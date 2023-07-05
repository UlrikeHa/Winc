from datetime import date, datetime, timedelta

# working with time
# using date.txt

def reset_time():
    new_date = date.today()
    with open('./data/date.txt', 'w') as f:
        f.write(str(new_date))
    
def get_date():
    with open('./data/date.txt', 'r') as f:
        return str(f.read())

def advance_time(days : int):
    format_str = '%Y-%m-%d' 
    now = get_date()
    new_date = (datetime.strptime(now, format_str)) + timedelta(days)
    with open('./data/date.txt', 'w') as f:        
        f.write(str(new_date.strftime('%Y-%m-%d')))

def set_new_date(date_str : str):
    format_str = '%Y-%m-%d' 
    new_date = datetime.strptime(date_str, format_str)
    with open('./data/date.txt', 'w') as f:
        f.write(str(new_date.strftime('%Y-%m-%d')))