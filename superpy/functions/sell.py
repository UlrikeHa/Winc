from functions.helpers import in_range, available_amount, get_product_information, update_storage, stock_counter, free_space, max_amount_buy
from functions.transfer import remove_from_inventory
from functions.time import reset_time

# -----------SELLING FUNCTION--------------------
# 1. set time to today
# 2. check if product is in product range
# 3. check if amount of product is in inventory
# 4. remove available amount from inventory
# 5. update used_space in storage.csv
# 6. print success or failure messages

def sell(product : str, amount : int = 1):
    reset_time()
    if in_range(product) is True:
        available = available_amount(product)
        if available == 0:
            print(f'Sorry, there is no {product} in store today!')
        if available <= amount and available != 0:
            for x in range(available):
                remove_from_inventory(product,'sold')                
            stock_counter(product, -available)
            if get_product_information(product,'cooled') == 'True':
                update_storage('cooling', -available)
            elif get_product_information(product,'frozen') == 'True':
                update_storage('freezing', -available)
            print(f'successfully sold {available}x {product}!')
        if available > amount:
            for x in range(amount):
                remove_from_inventory(product,'sold')                
            stock_counter(product, -amount)
            if get_product_information(product,'cooled') == 'True':
                update_storage('cooling', -amount)
            elif get_product_information(product,'frozen') == 'True':
                update_storage('freezing', -amount)
            print(f'successfully sold {amount}x {product}!')                                  
    else:
        print(f'Sorry, our store doesn\'t trade {product}')
           