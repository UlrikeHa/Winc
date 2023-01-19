# Do not modify these lines
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line
def create_passport(name, date_of_birth, place_of_birth, height, nationality):
    passport = {
        "name" : name,
        "date_of_birth" : date_of_birth,
        "place_of_birth" : place_of_birth,
        "height" : height,
        "nationality" : nationality  
        }
    if passport["nationality"] in get_countries():
        return passport

def add_stamp(passport, country):
    if "stamps" not in passport:
        passport["stamps"] = []
    if country != passport["nationality"] and country not in passport["stamps"]:
        passport["stamps"].append(country)
    return passport

def add_biometric_data(passport, type, data, date_recorded):
    if "biometric" not in passport:
        passport["biometric"] = {}

    passport["biometric"][type] = {
        "date" : date_recorded,
        "value" : data
        }
    return passport

passport = create_passport("Ulrich", "1977-01-21", "Dresden", 175, "Germany")
add_stamp(passport, "Spain")
add_stamp(passport, "Belgium")
add_biometric_data(passport, "eye_color_left", "blue", "31-01-2000")
add_biometric_data(passport, "eye_color_right", "brown", "31-01-2000")
print(passport)