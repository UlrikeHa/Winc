__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from os import mkdir, listdir, remove
import zipfile
from os.path import abspath

path = "./files/cache"

def clean_cache():
    try:
        mkdir(path)
    except FileExistsError:
        for file in listdir(path):
            remove(f'./files/cache/{file}')

def cache_zip(package_path : str, target : str):
    with zipfile.ZipFile(package_path, 'r') as package:
        package.extractall(target)

def cached_files():
    list = []
    for item in listdir(path):
        list.append(abspath(f"./files/cache/{item}"))
    return list

def find_password(my_list : list[str]):
    for item in my_list:
        with open(item, 'r') as content:
            for line in content:
                if "password" in line:
                    password = line.split()
                    return password[1]

print(find_password(cached_files()))
clean_cache()
