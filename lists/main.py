# Do not modify these lines
__winc_id__ = '6eb355e1a60f48a28a0bbbd0c88d9ab4'
__human_name__ = 'lists'

# Add your code after this line

def alphabetical_order(films):
    return sorted(films)

#films = ['v', 'f', 'r', 'd']
#print(alphabetical_order(films))

def won_golden_globe(film):
    winning_films = ['jaws', 'star wars: episode iv - the empire strikes back', 'e.t. the extra - terrestrial', 'memoirs of a geisha']
    return film.lower() in winning_films

#print(won_golden_globe('jaws'))
#print(won_golden_globe('Jaws'))
#print(won_golden_globe('Superman'))

def remove_toto_albums(all_albums):
    toto_albums = ["Fahrenheit", "The Seventh One", "Toto XX", "Falling in Between", "Toto XIV", "Old Is New"]
    for x in toto_albums:
        if x in all_albums:
            all_albums.remove(x)
    return all_albums

#print(remove_toto_albums(["test", "test2", "Fahrenheit", "test3", "Old Is New"]))


