import pandas as pd
import plotly as py
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

print('\n\n')

death = pd.read_csv('malaria_deaths.csv')
death.rename(columns={death.columns[3]: "death"}, errors='raise', inplace=True)
print(death.head())
# print(death.describe())

"""
fig = px.line(death, x='Year', y='death', color='Entity')
fig.show()
"""

df = px.data.gapminder().query("year==2007")
# print(df)
print(df.iloc[3, :])

fig = px.choropleth(
    death,
    locations="Code",
    color="death",  # lifeExp is a column of gapminder
    hover_name="Entity",  # column to add to hover information
    color_continuous_scale=px.colors.sequential.tempo,

    animation_frame="Year",

)
fig.show()


fig.write_html("v2.html")
