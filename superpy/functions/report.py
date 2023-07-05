import pandas as pd
from functions.time import get_date

# display inventory
# 1. short shows product, stock, max_stock using products.csv

def short_inventory():
    df = pd.read_csv(r'./data/products.csv')
    short = df[['name','stock','max_stock']]
    return short

# 2. full inventory shows product, buying date, expiration date using inventory.csv

def full_inventory():
    df = pd.read_csv(r'./data/inventory.csv')
    full = df[['name','date_buy','date_expire']].groupby(['name','date_buy','date_expire'])['date_buy'].agg(['count'])  
    return full.sort_values('name')
  
# ------------Profit Function---------------------
# 1. collect all buying and selling transactions from transfer.csv
# 2. filter by date or period for all products or one product of choice
# 3. count transactions for buy and sell
# 4. get total profit 
# 4. print messages and dataframe

def profit(date1 : str = get_date(), date2: str = None, product : str = None):
    df = pd.read_csv(r'./data/transfer.csv') 
    if date2 is None:
        if product is None:
            df = df[(df['date'] == date1) & (df['action'] != 'expired')]
            count_buy = df.loc[df['action'] == 'bought', 'price'].count()  
            count_sell = df.loc[df['action'] == 'sold', 'price'].count() 
            profit = (df.loc[df['action'] == 'sold', 'price'].sum()) - (df.loc[df['action'] == 'bought', 'price'].sum())
            header = f'Profit {date1}'
            total = f'total profit: {profit.round(2)} - transactions: bought {count_buy}, sold {count_sell}' 
        else:
            df = df[(df['date'] == date1) & (df['action'] != 'expired') & (df['name'] == product)]
            count_buy = df.loc[df['action'] == 'bought', 'price'].count()  
            count_sell = df.loc[df['action'] == 'sold', 'price'].count()
            profit = (df.loc[df['action'] == 'sold', 'price'].sum()) - (df.loc[df['action'] == 'bought', 'price'].sum())
            header = f'Profit {product} {date1}'
            total = f'total profit: {profit.round(2)} - transactions {product}: bought {count_buy}, sold {count_sell}'
    else:
        if product is None:
            df = df[(df['date'] >= min(date1, date2)) & (df['date'] <= max(date1, date2)) & (df['action'] != 'expired')]
            count_buy = df.loc[df['action'] == 'bought', 'price'].count()  
            count_sell = df.loc[df['action'] == 'sold', 'price'].count() 
            profit = (df.loc[df['action'] == 'sold', 'price'].sum()) - (df.loc[df['action'] == 'bought', 'price'].sum())
            header = f'Profit {min(date1, date2)} - {max(date1, date2)}'
            total = f'total profit: {profit.round(2)} - transactions: bought {count_buy}, sold {count_sell}'
        else:
            df = df[(df['date'] >= min(date1, date2)) & (df['date'] <= max(date1, date2)) & (df['action'] != 'expired') & (df['name'] == product)]
            count_buy = df.loc[df['action'] == 'bought', 'price'].count()  
            count_sell = df.loc[df['action'] == 'sold', 'price'].count() 
            profit = (df.loc[df['action'] == 'sold', 'price'].sum()) - (df.loc[df['action'] == 'bought', 'price'].sum())
            header = f'Profit {product} {min(date1, date2)} - {max(date1, date2)}'
            total = f'total profit: {profit.round(2)} - transactions {product}: bought {count_buy}, sold {count_sell}'

    df = df[['date','name','action','price']].groupby(['date','name','action'])['price'].agg(['count', 'sum']) 

    if sum(df['count']) == 0:
        if product is None:
            print('Nothing has been bought or sold during this day or period!') 
        else:
            print(f'{product} has not been bought or sold during this day or period!')
    else:
        print('------------------------------------------------------------------------') 
        print(header)  
        print('------------------------------------------------------------------------')  
        print(df)
        print('------------------------------------------------------------------------')  
        print(total)
        print('------------------------------------------------------------------------') 
  
# ------------Revenue Function---------------------
# 1. collect all selling transactions from transfer.csv
# 2. filter by date or period for all products or one product of choice
# 3. get total of columns 'count' and 'sum' 
# 4. print messages and dataframe

def revenue(date1 : str = get_date(), date2: str = None, product : str = None):
    df = pd.read_csv(r'./data/transfer.csv') 
    if date2 is None:
        if product is None:
            df = df[(df['date'] == date1) & (df['action'] == 'sold')]
            total_count = len(df. index)  
            total_sum = format(sum(df['price']),'.2f')
            header = f'Revenue {date1}'
            total = f'total revenue is {total_sum} for {total_count} product(s)' 
        else:
            df = df[(df['date'] == date1) & (df['action'] == 'sold') & (df['name'] == product)]
            total_count = len(df. index)  
            total_sum = format(sum(df['price']),'.2f')
            header = f'Revenue {product} {date1}'
            total = f'total revenue is {total_sum} for {total_count} {product}'
    else:
        if product is None:
            df = df[(df['date'] >= min(date1, date2)) & (df['date'] <= max(date1, date2)) & (df['action'] == 'sold')]
            total_count = len(df. index) 
            total_sum = format(sum(df['price']),'.2f')
            header = f'Revenue {min(date1, date2)} - {max(date1, date2)}'
            total = f'total revenue is {total_sum} for {total_count} product(s)'
        else:
            df = df[(df['date'] >= min(date1, date2)) & (df['date'] <= max(date1, date2)) & (df['action'] == 'sold') & (df['name'] == product)]
            total_count = len(df. index)  
            total_sum = format(sum(df['price']),'.2f')
            header = f'Revenue {product} {min(date1, date2)} - {max(date1, date2)}'
            total = f'total revenue is {total_sum} for {total_count} {product}'

    df = df[['date','name','action','price']].groupby(['date','name','action'])['price'].agg(['count', 'sum']) 

    if sum(df['count']) == 0:
        if product is None:
            print('Nothing has been sold during this day or period!') 
        else:
            print(f'{product} has not been sold during this day or period!')
    else:
        print('--------------------------------------------------------') 
        print(header)  
        print('--------------------------------------------------------')  
        print(df)
        print('--------------------------------------------------------')  
        print(total)
        print('--------------------------------------------------------') 