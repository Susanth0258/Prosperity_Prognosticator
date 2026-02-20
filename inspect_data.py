import pandas as pd
try:
    df = pd.read_csv('dataset/startup_data.csv')
    print("Columns:", df.columns.tolist())
    print(df.head())
except Exception as e:
    print(e)
