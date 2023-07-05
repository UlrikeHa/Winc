import csv
import pandas as pd
import pandas.io.common
from datetime import date, datetime, timedelta
from functions.time import get_date

# create an id for a new row in existing csv file + error handling

def get_new_id(csv_file : str) -> int:
    try:
        df = pd.read_csv(f'./data/{csv_file}')   
        highest_id = df.iloc[-1, df.columns.get_loc('id')]
        new_id = highest_id + 1
        return new_id
    
    except (pandas.errors.EmptyDataError, IndexError) as e:
        return 1

    except FileNotFoundError:
        print(csv_file + " not found")

# reading a csv file and storing in a list of dictionaries

def read_csv_as_dict(csv_file : str):
     with open(f'./data/{csv_file}') as file:
        list_of_rows = [] 
        reader = csv.DictReader(file)
        for row in reader:
            list_of_rows.append(row)
        return list_of_rows
              

# get a value from a csv file knowing another value in the same row
# 1. find specific row in csv file and store it in a dictionary

def get_row(csv_file : str, known_tuple : tuple) -> dict:
    with open(f'./data/{csv_file}') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if known_tuple in row.items():
                return row

# 2. get a value from that dictionary

def get_value(row : dict, key : str):
    value = row.get(key)
    return value

#fetch an id (-> product_id) from products.csv

def get_product_id(product : str) -> int:
    value = get_value(get_row("products.csv", ("name", product)),"id")
    return int(value)

# fetch a specific value from products.csv

def get_product_information(product : str, column : str):
    value = get_value(get_row("products.csv", ("name", product)),column)
    return value

# create an expiration date using date.txt and products.csv

def get_expiration_date(product : str) -> date:
    with open("./data/date.txt", mode="r") as d:
        today = date.fromisoformat(d.read())
    try:
        expiration_date = today + timedelta(int(get_product_information(product, 'expire')))
    except ValueError:
        expiration_date = '-'    
    return expiration_date

# check if product is in products.csv (product range of the store)

def in_range(product : str) -> bool:
    if get_row("products.csv", ("name", product)) == None:
        return False
    else:
        return True

# check how many pieces of a product may be bought by the store using products.csv

def max_amount_buy(product : str) -> int:
    information = get_row("products.csv", ("name", product))
    limit = int(information['max_stock'])
    in_stock = int(information['stock'])
    max_amount = limit - in_stock
    return max_amount
   
# check how many pieces of a product are available in store using inventory.csv

def available_amount(product : str)-> int:
    count = 0
    with open(f'./data/inventory.csv') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if ("name", product) in row.items():
                count +=1
    return count

# check free storage space using storage.csv

def free_space(product : str) ->int:
    max_space = 0
    used_space = 0
    if get_product_information(product, 'cooled') == 'True':
        with open(f'./data/storage.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if ('cooling', 'True') in row.items():
                    max_space += int(row['max_space'])
                    used_space += int(row['used_space'])
                                        
    elif get_product_information(product, 'frozen') == 'True':
        with open(f'./data/storage.csv') as file:
            reader = csv.DictReader(file)
            for row in reader:
                if ('freezing', 'True') in row.items():
                    max_space += int(row['max_space'])
                    used_space += int(row['used_space'])
    
    else:
        max_space = 999999999

    return max_space - used_space 

# check if purchase fits in storage space

def check_valid_amount_buy(product : str, amount : int) -> bool:
    if amount <= 0: 
        print(f'amount can\'t be negative')
        return False      
    if amount <= int(max_amount_buy(product)) and int(free_space(product)):   
        return True
    else:
        print(f'Sorry, you can\'t buy {amount}x {product}!')
        return False
    
# update 'used_space' in storage.csv

def update_storage(action : str, amount : int):    
    storage_units = read_csv_as_dict('storage.csv') 
    amount = amount
    for row in storage_units:
        if (action, 'True') in row.items():
            if amount > 0:            
                free_space = int(row['max_space']) - int(row['used_space'])
                if free_space >= amount:
                    new_value = int(row['used_space']) + amount
                    row['used_space'] = str(new_value)
                    amount = 0
                else:
                    row['used_space'] = row['max_space']
                    amount = amount - free_space
            if amount < 0:
                if int(row['used_space']) >= abs(amount):
                    row['used_space'] = int(row['used_space']) + amount
                    amount = 0                    
                else:
                    amount = amount + int(row['used_space'])
                    row['used_space'] = '0'
                    
    with open(f'./data/storage.csv', 'w', newline='') as file:
        header = ['id','name','max_space','used_space','cooling','freezing']
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(storage_units)

# update 'stock' in products.csv    

def stock_counter(product : str, amount : int):
    df = pd.read_csv(r'./data/products.csv')
    df.loc[df['name'] == product,'stock'] += amount
    df.to_csv(r'./data/products.csv', index = False)
    
# check format of date input

def validate_date(date):
    if date != None:            
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            print(f"Incorrect date {date}. Please use the following format YYYY-MM-DD")
            return False
        else:
            return True      

# check if product has almost expired using sale in products.csv  

def sale(inventory_id : int) -> bool:
    df = pd.read_csv(r'./data/inventory.csv', index_col='id')    
    product = df.at[inventory_id,'name']
    with open("./data/date.txt", mode="r") as d:
        today = date.fromisoformat(d.read())
    try:
        ed = date.fromisoformat(df.at[inventory_id,'date_expire'])
        start_sale = ed + timedelta(int(get_product_information(product, 'sale')))
        if start_sale < today:
            return True
        if start_sale >= today:
            return False
    except ValueError:
        return False   
    
