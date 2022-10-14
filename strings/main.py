# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

from operator import truediv

scorer_0 = "Ruud Gullit"
scorer_1 = "Marco van Basten"

goal_0 = 32
goal_1 = 54

# who scored when
scorers = scorer_0 + " " + str(goal_0) + ", " + scorer_1 + " " + str(goal_1)
print(str(scorers))

# report goals
report = f'{scorer_0} scored in the {goal_0}nd minute\n{scorer_1} scored in the {goal_1}th minute'
print(str(report))

# split playername using find
player = "Sergei Aleinikov"
find_first_name = player.find("S")
find_last_name = player.find("A")
print(str(find_first_name) + str(find_last_name))

first_name = player[0:6]
last_name = player[7:]
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

