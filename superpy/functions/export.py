import pandas as pd
from functions.time import get_date
from pathlib import Path

# export transfers by day, month or year
# 1. collect transactions from transfer.csv
# 2. filter by day, month or year
# 3. write df to data/reports/day,month,year/{filter}.csv
# 4. print messages

def export(date):
    df = pd.read_csv(r'./data/transfer.csv')
    df['date'] = pd.to_datetime(df['date'], format='%Y-%m-%d')
    file_out = f'{date}.csv'
    if len(date) == 4:
        df = df[df['date'].dt.strftime('%Y') == date]
        dir_out = Path('data/reports/year')
        dir_out.mkdir(parents=True, exist_ok=True)
        

    if len(date) == 7:
        df = df[df['date'].dt.strftime('%Y-%m') == date]
        dir_out = Path('data/reports/month')
        dir_out.mkdir(parents=True, exist_ok=True)
        

    if len(date) == 10:
        df = df[df['date'].dt.strftime('%Y-%m-%d') == date]
        dir_out = Path('data/reports/day')
        dir_out.mkdir(parents=True, exist_ok=True)
    
    if df.empty:
        print(f'export failed. no transfers during this day or period')
    else:
        sorted_df = df[['date','action','name','price','inventory_id']].sort_values(by=['date', 'action', 'name'])
        sorted_df.to_csv(dir_out/file_out, index=False)    
        print(f'export successful')


