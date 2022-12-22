# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line

def farm_action(weather, time, milk, location, season, slurry, grass):

    if location == 'pasture' and (time == 'night' or  weather == 'rainy'):
        return 'take cows to cowshed'

    elif milk == True and location == 'cowshed':
        return 'milk cows'

    elif milk == True and location == 'pasture':
        return 'take cows to cowshed\nmilk cows\ntake cows back to pasture'

    elif slurry == True and weather != 'windy' and weather != 'sunny' and location == 'cowshed':
        return 'fertilize pasture'

    elif slurry == True and weather != 'windy' and weather != 'sunny' and location == 'pasture':
        return 'take cows to cowshed\nfertilize pasture\ntake cows back to pasture'

    elif grass == True and weather == 'sunny' and season == 'spring' and location == 'cowshed':
        return 'mow grass'

    elif grass == True and weather == 'sunny' and season == 'spring' and location == 'pasture':
        return 'take cows to cowshed\nmow grass\ntake cows back to pasture'

    else:
        return 'wait'


# some tests  
print(farm_action('sunny', 'day', False, 'pasture', 'spring', False, True))

