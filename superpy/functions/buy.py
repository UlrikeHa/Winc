from functions.helpers import in_range, check_valid_amount_buy, get_product_information, update_storage, stock_counter, free_space, max_amount_buy
from functions.transfer import add_to_inventory
from functions.time import reset_time

# -----------BUYING FUNCTION--------------------
# 1. set time to today
# 2. check if product is in range
# 3. check if amount fits in storage (max_stock in products.csv, free_space in freezer and fridge)
# 4. add products to inventory.csv
# 5. update stock in products.csv
# 6. update used_space in storage.csv
# 7. print succes or failure message with reason

def buy(product : str, amount : int = 1):
    reset_time()
    if in_range(product) is True:
        if check_valid_amount_buy(product, amount) is True:
            for x in range(amount):
                add_to_inventory(product)
            stock_counter(product, amount)
            if get_product_information(product,'cooled') == 'True':
                update_storage('cooling', amount)
            elif get_product_information(product,'frozen') == 'True':
                update_storage('freezing', amount)
            print(f'successfully bought {amount}x {product}!')  
        else:
            if free_space(product) <= max_amount_buy(product):
                print(f'Not enough space in our cooling or freezing storage. You can buy only {free_space(product)}x {product}!')  
            else:
                print(f'You can buy only {max_amount_buy(product)}x {product}! Maximum in stock reached.')                
    else:
        print(f'Sorry, our store doesn\'t trade {product}')
           