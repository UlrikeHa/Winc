from helpers import get_countries


""" Leave this untouched. Wincpy uses it to match this assignment with the
tests it runs. """
__winc_id__ = "c545bc87620d4ced81cbddb8a90b4a51"
__human_name__ = "for"


""" Write your functions here. """

def shortest_names(countries):
    short = 0
    shortlist = []
    for x in countries:
        if short == 0 or len(x) < short:
            short = len(x)
    for x in countries:
        if len(x) == short:
            shortlist.append(x)
    return shortlist
        
def most_vowels(countries):
    vowels = ["a", "e", "i", "o", "u"]
    count_vowels = []
    for country in countries:
        count_vowels.append(len([x for x in country if x.lower() in vowels]))

    count_vowels = sorted(tuple(zip(count_vowels, countries)), reverse = True)

    most_v, sorted_countries = zip(*count_vowels)

    return sorted_countries[:3]

def alphabet_set(countries):
    import string
    alphabet = list(string.ascii_lowercase)
    wanted_letters = alphabet
    dif_letters = []
    count_letters = []
    most_dif_letters = []
    country_list = []

    while len(wanted_letters) > 0:

        for country in countries:
            country_lower_set = set(country.lower()) 
            dif_letters.append(len([x for x in country_lower_set if x.lower() in wanted_letters]))
        count_letters = sorted(tuple(zip(dif_letters, countries)), reverse = True)
        letters, sorted_countries = zip(*count_letters)

        most_dif_letters = sorted(list(set(sorted_countries[0].lower())))

        for letter in most_dif_letters: 
            if letter in wanted_letters:
                wanted_letters.remove(letter)

        dif_letters = []
        count_letters = []
        most_dif_letters = []

        country_list.append(sorted_countries[0]) 
        
    return country_list   


# This block is only run if this file is the entrypoint; python main.py
# It is not run if it is imported as a module: `from main import *`
if __name__ == "__main__":
    countries = get_countries()
    shortest_names(countries)
    most_vowels(countries)
    print(alphabet_set(countries))
    