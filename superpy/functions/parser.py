import argparse
import sys
from functions.time import get_date

def parser():

    # add parser for cmdline input

    parser = argparse.ArgumentParser(prog = 'SuperPy ', description = 'This is SuperPy! - a commandline tool to manage the inventory of a Supermarket')
    subparsers = parser.add_subparsers(dest='command')

    # create subparsers buy, sell, inventory, revenue, profit, status, remove, time, export

    buy = subparsers.add_parser('buy', help = 'buy a product')
    buy.add_argument('-p','--product', required = True, help='name of the product', type = str.lower)
    buy.add_argument('-a','--amount', default=1, help='the amount to buy', type = int)
    
    sell = subparsers.add_parser('sell', help = 'sell a product')
    sell.add_argument('-p','--product', required = True, help='name of the product', type = str.lower)
    sell.add_argument('-a','--amount', default = 1, help = 'the amount to sell', type = int)
   
    inventory = subparsers.add_parser('inventory', help = 'shows today\'s inventory')
    inventory.add_argument('action', choices = ['short', 'full'], help = 'short gives a summary of our stock. full shows more information per product')

    revenue = subparsers.add_parser('revenue', help = 'shows revenue per date, period and/or product')
    revenue.add_argument('-p','--product', help='name of the product', type = str.lower)
    revenue.add_argument('-d1','--date1', default = get_date(), type = str)
    revenue.add_argument('-d2','--date2', type = str)

    profit = subparsers.add_parser('profit', help = 'shows profit per date, period and/or product')
    profit.add_argument('-p','--product', help='name of the product', type = str.lower)
    profit.add_argument('-d1','--date1', default = get_date(), help='date or starting date used to filter transactions', type = str)
    profit.add_argument('-d2','--date2', help='end date used to filter transactions', type = str)
            
    status = subparsers.add_parser('status', help='gives an overview of stock, storage space, expiration')
    status.add_argument('action', choices = ['storage', 'stock', 'expired', 'all'])
        
    remove = subparsers.add_parser("remove", help='remove data from csv. be carefull data can be lost')
    remove.add_argument('action', choices = ['expired', 'old'], help = 'removes expired products from inventory or transfers older than 2 years')
    
    time = subparsers.add_parser('time', help = 'manipulate time: -a --advance, -s --set, -r --reset')
    time.add_argument('action', choices = ['advance', 'set', 'reset'])
    time.add_argument('-d','--days', required='advance' in sys.argv, type = int, help='advance time by amount x day(s)')
    time.add_argument('-n', '--new', required='set' in sys.argv, type = str, help='set a new date: format "2000-01-01"')

    export = subparsers.add_parser('export', help = 'export parts of transfer data to new csv files')
    export.add_argument('-d', '--date', required = True, type = str, help='export by day: format "2000-01-01", by month: format "2000-01", by year: format "2000"')
    
    return parser.parse_args() 