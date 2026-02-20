import pandas as pd
df = pd.read_csv('dataset/startup_data.csv')
for col in df.columns:
    print(col)
