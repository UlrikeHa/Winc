# Do not modify these lines
__winc_id__ = '62311a1767294e058dc13c953e8690a4'
__human_name__ = 'casting'

# Add your code after this line

leek_price = 2
print(str(f'Leek is {leek_price} euro per kilo.'))

amount = "leek 4"
find_amount = amount.find(" ")
leek_amount = int(amount[find_amount + 1])

sum_total = leek_price * leek_amount
print(sum_total)

broccoli_price = 2.34
broccoli_order = 1.6

price_total = broccoli_price * broccoli_order
price_total = round(price_total,2)

print(str(broccoli_order) + "kg broccoli costs " + str(price_total) + "e")