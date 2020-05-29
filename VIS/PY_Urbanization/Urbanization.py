import pandas as pd
import plotly.graph_objects as go

# loading the data
data_path = "DATA/urban-vs-rural-majority.csv"
df = pd.read_csv(data_path)

# remove everything before 1950
df = df[df['Year'] >= 1950]

# group by countries
grouped_df = df.groupby(['Entity'])

# plot each group to a line
lines = [go.Scatter(
    name=g[0],
    line_shape='spline',
    line=dict(width=0.5),
    x=g[1]['Year'],
    y=g[1]['Urban (%)']
) for g in grouped_df]

# add lines to figure
fig = go.Figure(data=lines)

# set the theme
fig.layout.template = 'plotly_dark'

# add meta data and plot range
fig.update_layout(title='Urbanization per Countries',
                  xaxis_title='Year',
                  yaxis_title='Percentage of Population Living in Urban Areas',
                  yaxis=dict(range=[0, 100]),
                  xaxis=dict(range=[1950, 2050]),
                  )

# write plot to html
html_path = "OUT/Urbanization.html"
fig.write_html(html_path)

# show theplot
# fig.show()
