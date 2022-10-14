# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(str(scorers))

report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'
print(str(report))

player = "Sergei Aleinikov"
find_middle = player.find(" ")
print(str(find_middle))

first_name = player[:find_middle]
last_name = player[find_middle+1:]
last_name_len = len(last_name)
print(last_name_len)

name_short = first_name[0] + ". " + last_name
print(name_short)

x = len(first_name)
chant = ((first_name + "! ") * x)
chant = chant[:-1]      # remove last charakter
print(chant)

# test that chant doesn't end with space
good_chant = chant[-1] != " "
print(good_chant)

