import pandas as pd

# loading the data
data_path = "DATA/urban-vs-rural-majority.csv"
df = pd.read_csv(data_path, index_col=1)

# group by countries
grouped_df = df.groupby(['Entity'])

for g in grouped_df:
    print(g)
    break
# print(test)
