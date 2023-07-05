import pandas as pd
from functions.time import get_date, reset_time
from functions.helpers import sale

# ---------------status of products in store-----------------
# 1. reset time
# 2. read products.csv
# 3. filter by products currently not in store 
# 4. filter by products currently under 15% of max_stock 
# 5. print messages for different conditions

def status_stock():
    reset_time()
    df = pd.read_csv(r'./data/products.csv')
    empty = df[['name']][(df['stock'] == 0)]
    small = df[['name']][(df['stock'] <= (df['max_stock']*0.15)) & (df['stock'] > 0)]
    print('---------------------------------------------------')
    print(f'{get_date()} Status:')
    print('---------------------------------------------------')
    if empty.empty and small.empty:
        print(f'All products are in stock!')
        print('---------------------------------------------------')
    elif empty.empty:
        if len(small.index) == 1:
            print(f'All products are in stock, but following product could use restocking!')
        else:
            print(f'All products are in stock, but following {len(small. index)} products could use restocking!')
        for index, row in small.iterrows():
            print(row["name"])
        print('---------------------------------------------------')    
    elif small.empty:
        if len(empty.index) == 1:
            print(f'Following product is not in stock!')
        else:
            print(f'Following {len(empty. index)} products are not in stock!')
        for index, row in empty.iterrows():
            print(row["name"])
        print('---------------------------------------------------')
        print('You should place an order!')
        print('---------------------------------------------------')
    else:
        if len(empty.index) == 1:
            print(f'Following product is not in stock!')
        else:
            print(f'Following {len(empty. index)} products are not in stock!')
        for index, row in empty.iterrows():
            print(row["name"])
        print('---------------------------------------------------')
        if len(small.index) == 1:
            print(f'Following product could also use restocking!')
        else:
            print(f'Following {len(small. index)} products could also use restocking!')
        for index, row in small.iterrows():
            print(row["name"])
        print('---------------------------------------------------')
        print('You should place an order!')
        print('---------------------------------------------------')

# ---------------status of expired products in store-----------------
# 1. reset time
# 2. read inventory.csv
# 3. get expired products (dfe)
# 4. get almost expired products (dfs)
# 5. print messages for different conditions

def status_expired():
    reset_time()
    today = get_date()   
    df = pd.read_csv(r'./data/inventory.csv')
    df['sale'] = df.apply(lambda row: sale(row.id), axis = 1)
    dfe = df[(df['date_expire'] <= today) & (df['date_expire'] != '-')]
    dfs = df[(df['date_expire'] > today) & (df['sale'] == True)]  
    print('---------------------------------------------------------------------')
    print(f'{get_date()} Status:')
    print('---------------------------------------------------------------------')
    
    if dfe.empty:
        print(f'There are no expired products in store today')
    else:
        print(f'Following products have expired!\n')
        print(f'ID Name')
        for index, row in dfe.iterrows():
            print(row['id'],row['name'])
        print(f'\nPlease remove expired product(s) from Superpy and our store!')
        print(f'>>> python super.py remove expired\n')
    
    if dfs.empty:
        print(f'There are no new items in sale today')
    else:
        count = 0
        print(f'Following products have almost expired!\n')
        print(f'ID Name')
        for index, row in dfs.iterrows():    
            print(row['id'],row['name']) 
            count += 1
        print(f'\n{count} item(s) need to get marked as sale product with reduced pricing!')
    print('---------------------------------------------------------------------')
 
# ---------------------Status Storage---------------------------------
# 1. reset time
# 2. get information from storage.csv
# 3. filter by cooling and freezing
# 4. sum max_space and used_space columns
# 5. print messages depending on free space in storage

def status_storage():
    reset_time()
    df = pd.read_csv(r'./data/storage.csv')
    dfc = df[df['cooling'] == True]
    dff = df[df['freezing'] == True]
    max_cooling = dfc['max_space'].sum()
    max_freezing = dff['max_space'].sum()
    used_space_cooling = dfc['used_space'].sum()
    used_space_freezing = dff['used_space'].sum()
    free_space_cooling = max_cooling - used_space_cooling
    free_space_freezing = max_freezing - used_space_freezing

    print('-------------------------------------------------------------------------------')
    print(f'{get_date()} Status:') 
    print('-------------------------------------------------------------------------------')
    print(f'cooling storage:\n')    
    dfc = dfc[['name', 'used_space', 'max_space']]
    print(dfc.to_string(index=False))
    print('-------------------------------------------------------------------------------')
    print(f'free cooling space: {free_space_cooling}')
    if used_space_cooling == max_cooling:
        print(f'Our fridges are full! Don\'t buy more products! You could think about a new fridge!')
    if used_space_cooling >= max_cooling * 0.9:
        print(f'Our fridges are almost full! Be carefull while ordering more products!')
    if used_space_cooling == 0:
        print(f'All fridges are empty! Please turn of fridges or buy some products!')
    if used_space_cooling <= max_cooling * 0.45:
        print(f'Our fridges are not filled well! Please turn of fridges or buy some products!')
    else:
        print(f'Our fridges are filled well. There is not too much unused space!')
    print('-------------------------------------------------------------------------------')
    print(f'freezing storage:\n')
    dff = dff[['name', 'used_space', 'max_space']]
    print(dff.to_string(index=False))
    print('-------------------------------------------------------------------------------')
    print(f'free freezing space: {free_space_freezing}')    
    if used_space_freezing == max_freezing:
        print(f'Our freezers are full! Don\'t buy more products! You could think about a new freezer!')
    if used_space_freezing >= max_freezing * 0.9:
        print(f'Our freezers are almost full! Be carefull while ordering more products!')
    if used_space_freezing == 0:
        print(f'All freezers are empty! Please turn of freezers or buy some products!')
    if used_space_freezing <= max_freezing * 0.45:
        print(f'Our freezers are not filled well! Please turn of freezers or buy some products!')
    else:
        print(f'Our freezers are filled well. There is not too much unused space!')
    print('-------------------------------------------------------------------------------')


# ------------------------- summary status -----------------------------------

def status_all():
    reset_time()
    today = get_date()  
    
    print('---------------------------------------------------------------------')
    print(f'{get_date()} Status:') 
    print('---------------------------------------------------------------------')

   # show status expiration
    print(f'Expiration\n')
       
    df = pd.read_csv(r'./data/inventory.csv')
    df['sale'] = df.apply(lambda row: sale(row.id), axis = 1)
    dfe = df[(df['date_expire'] <= today) & (df['date_expire'] != '-')]
    dfs = df[(df['date_expire'] > today) & (df['sale'] == True)]   

    if dfe.empty:
        print(f'There are no expired products in store today')
    else:
        row_count = dfe.shape[0]
        print(f'{row_count} product(s) expired')
    
    if dfs.empty:
        print(f'There are no new products on sale today')
    else:
        row_count = dfs.shape[0]
        print(f'{row_count} new product(s) on sale')
    print(f'check full status: >>> python super.py status expired')
    print('---------------------------------------------------------------------')

# show status stock

    print(f'Stock information\n')

    df = pd.read_csv(r'./data/products.csv')
    empty = df[['name']][(df['stock'] == 0)]
    small = df[['name']][(df['stock'] <= (df['max_stock']*0.15)) & (df['stock'] > 0)]
    count_empty = empty.shape[0]
    count_small = small.shape[0]
    if empty.empty and small.empty:
        print(f'All products are in stock')
    elif empty.empty:
        print(f'All products are in stock, but {count_small} product(s) could use restocking! ')
        print(f'check full status: >>> python super.py status stock')
    elif small.empty:
        print(f'{count_empty} product(s) not in stock')
        print(f'check full status: >>> python super.py status stock')
    else:
        print(f'{count_empty} product(s) not in stock.')
        print(f'{count_small} product(s) could use restocking!')
        print(f'check full status: >>> python super.py status stock')

    print('---------------------------------------------------------------------')

# show status storage

    print(f'Storage\n')

    df = pd.read_csv(r'./data/storage.csv')
    dfc = df[df['cooling'] == True]
    dff = df[df['freezing'] == True]
    max_cooling = dfc['max_space'].sum()
    max_freezing = dff['max_space'].sum()
    used_space_cooling = dfc['used_space'].sum()
    used_space_freezing = dff['used_space'].sum()
       
    print(f'used cooling space: {used_space_cooling}  max: {max_cooling}')
    print(f'used freezing space: {used_space_freezing}  max: {max_freezing}')
    print(f'check full status: >>> python super.py status storage')

    print('---------------------------------------------------------------------')
