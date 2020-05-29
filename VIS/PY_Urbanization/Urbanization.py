import pandas as pd
import plotly.graph_objects as go
import numpy as np

# loading the data
data_path = "DATA/urban-vs-rural-majority.csv"
df = pd.read_csv(data_path)

# remove everything before 1950
df = df[df['Year'] >= 1950]

# group by countries
grouped_df = df.groupby(['Entity'])

# plot
lines = [go.Scatter(
    x=g[1]['Year'],
    y=g[1]['Urban (%)']
) for g in grouped_df]

fig = go.Figure(data=lines)
fig.layout.template = 'plotly_dark'
fig.show()
