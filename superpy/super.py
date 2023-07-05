# Imports
from functions.parser import parser
from functions.report import short_inventory, full_inventory, revenue, profit
from functions.buy import buy
from functions.sell import sell
from functions.transfer import clean_transfers, delete_expired
from functions.status import status_stock, status_expired, status_storage, status_all 
from functions.time import reset_time, advance_time, set_new_date, get_date
from functions.export import export
from functions.helpers import validate_date

# Do not change these lines.
__winc_id__ = "a2bc36ea784242e4989deb157d527ba0"
__human_name__ = "superpy"


# Your code below this line.
def main():
    args = parser()
    input = args.command
            
    if input == 'buy':
        if args.amount <= 0:
            print(f'-a, --amount can\'t be negative')
        else:
            buy(args.product, args.amount)

    if input == 'sell':
        if args.amount <= 0:
            print(f'-a, --amount can\'t be negative')
        else:
            sell(args.product, args.amount)

    if input == 'inventory':
        if args.action == 'short':
            df = short_inventory()
            print(df.to_string(index=False))
        if args.action == 'full':
            df = full_inventory()
            print(df.to_string(index=True))

    if input == 'revenue':
        if validate_date(args.date1) and validate_date(args.date2) != False:
            revenue(args.date1, args.date2, args.product)

    if input == 'profit':
        if validate_date(args.date1) and validate_date(args.date2) != False:
            profit(args.date1, args.date2, args.product)
       
    if input == 'status':
        if args.action == 'all':
            status_all()
        if args.action == 'storage':
            status_storage()    
        if args.action == 'stock':
            status_stock()            
        if args.action == 'expired':
            status_expired()            

    if input == 'remove':
        if args.action == 'expired':
            delete_expired()
        if args.action == 'old':
            clean_transfers()

    if input == 'time':    
        if args.action == 'advance':
            advance_time(args.days)
        if args.action == 'set':
            if validate_date(args.new) == True:
                set_new_date(args.new)       
        if args.action == 'reset':
            reset_time()  
        print(f'the internal date is {get_date()}')

    if input == 'export':
        export(args.date)    
      
if __name__ == "__main__":
    main()