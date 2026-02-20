import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
try:
    df = pd.read_csv('dataset/startup_data.csv')
    print("Columns:", list(df.columns))
    print(df['status'].value_counts() if 'status' in df.columns else "No 'status' column")
except Exception as e:
    print(e)
