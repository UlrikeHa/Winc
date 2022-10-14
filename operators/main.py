# Do not modify these lines
__winc_id__ = 'd0d3cdcefbb54bc980f443c04ab3a9eb'
__human_name__ = 'operators'

# Add your code after this line

language_spain = "Castillian Spanish"   #teststatus
language_switzerland = "German"
print(language_spain == language_switzerland)

religion_spain = "Roman Catholic"
religion_switzerland = "Roman Catholic"
print(religion_spain == religion_switzerland)

capitol_spain = "Madrid"
capitol_switzerland = "Bern"
print(len(capitol_spain) != len(capitol_switzerland))

gdp_growth_spain = 1.95
gdp_growth_switzerland = 1.11
print(gdp_growth_switzerland > gdp_growth_spain)

population_growth_spain = 0.13
population_growth_switzerland = 0.65
print(population_growth_spain < 1 and population_growth_switzerland < 1)

population_spain = 47163418
population_switzerland = 8508698
print(population_spain > 10000000 or population_switzerland > 10000000)

print((population_spain > 10000000 and not population_switzerland > 10000000) or (population_switzerland > 10000000 and not population_spain > 10000000))