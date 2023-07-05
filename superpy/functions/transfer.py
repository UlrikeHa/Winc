import csv
import pandas as pd
from dateutil.relativedelta import relativedelta
from functions.helpers import get_date, get_new_id, get_product_information, get_expiration_date, get_row, get_value, read_csv_as_dict, sale, stock_counter, update_storage
from functions.time import reset_time
from datetime import date

# write to inventory.csv

def add_to_inventory(product : str):
    with open(f'./data/inventory.csv', 'a', newline='') as file:
        header = ['id','name','date_buy','date_expire']
        new_id = get_new_id('inventory.csv')
        add_transfer(product,'bought',new_id)
        date_buy = get_date()
        date_expire = get_expiration_date(product)
        writer = csv.DictWriter(file, header)
        writer.writerow({
            'id': new_id,           
            'name': product,
            'date_buy': date_buy,
            'date_expire': date_expire
                         })

# write to transfer.csv -> used for buying, selling and removing expired products

def add_transfer(product : str, action : str, inventory_id : int):  
    with open(f'./data/transfer.csv', 'a', newline='') as file:
        header = ['id','inventory_id','name','action','price','date']
        new_id = get_new_id('transfer.csv')
        transfer_date = get_date()
        price = 0
        if action == 'bought':
            price = get_product_information(product, 'buy')
        if action == 'sold':
            if sale(inventory_id) is False:
                price = get_product_information(product, 'sell')
            else:
                price = round(float(get_product_information(product, 'sell')) * 0.65, 2)
        if action == 'expired':
            price = 0
        writer = csv.DictWriter(file, header)
        writer.writerow({
            'id': new_id,
            'inventory_id': inventory_id,        
            'name': product,
            'action': action,
            'price': price,
            'date': transfer_date
                         })

# remove sold items from inventory (possibility to extend this by actions: donated or moved)

def remove_from_inventory(product : str, action : str):
    row_to_remove = get_row("inventory.csv", ("name", product))
    add_transfer(product,action,int(get_value(row_to_remove, 'id')))
    list_temp = read_csv_as_dict('inventory.csv')
    list_temp.remove(row_to_remove)
    with open(f'./data/inventory.csv', 'w', newline='') as file:
        header = ['id','name','date_buy','date_expire']
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(list_temp)

# --------------- function to remove expired products ------------------
# 1. set date to today
# 2. fetch rows (dictionaries) from inventory with expiration date today and older
# 3. add transfer to transfer.csv for every row to remove
# 4. update stock in products.csv
# 5. update changes in inventory.csv
# 6. update used_space in storage.csv
# 7. print message

def delete_expired():
    reset_time()
    expired = []
    list_temp = read_csv_as_dict('inventory.csv')
    today = get_date()
    count = 0
    for row in list_temp:
        if row['date_expire'] <= today and row['date_expire'] != '-':
            expired.append(row)
    for row in expired:        
        list_temp.remove(row)
        add_transfer(row['name'],'expired', int(row['id']))
        stock_counter(row['name'], -1)
        if get_product_information(row['name'],'cooled') == 'True':
            update_storage('cooling', -1)
        elif get_product_information(row['name'],'frozen') == 'True':
            update_storage('freezing', -1)
        count += 1
    with open(f'./data/inventory.csv', 'w', newline='') as file:
        header = ['id','name','date_buy','date_expire']
        writer = csv.DictWriter(file, header)
        writer.writeheader()
        writer.writerows(list_temp)
    if count != 0:
        print(f'Successfully removed {count}x expired product(s) from inventory!')
    else:
        print(f'There are no expired products in our store today!')

# delete old transfers (2 years and older)

def clean_transfers():
    reset_time()
    df = pd.read_csv(r'./data/transfer.csv')
    end_date = str(date.fromisoformat(get_date()) - relativedelta(years = 2))
    df.drop(df[df['date'] <= end_date].index, inplace = True)
    df.to_csv(r'./data/transfer.csv', index = False)
    print(f'Successfully removed all transfers older than 2 years')
            