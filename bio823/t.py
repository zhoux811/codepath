import pandas as pd
import plotly as py
import plotly.graph_objects as go
import numpy as np
import plotly.express as px

death_age = pd.read_csv('malaria_deaths_age.csv')
print(death_age.head())
# print(death_age.describe())

print('\n\n')

print(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)])
print(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)]['deaths'])
print(sum(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)]['deaths']))

print('\n\n')

death = pd.read_csv('malaria_deaths.csv')
print(death.head())
# print(death.describe())


death = pd.read_csv('malaria_deaths.csv')
print(death.head())
print(death.describe())

death = pd.read_csv('malaria_deaths.csv')
death.rename(columns={death.columns[3]: "death"}, errors='raise', inplace=True)
# print(death.head())


df = px.data.gapminder()
fig = px.scatter(
    df, x="gdpPercap",
    y="lifeExp",
    animation_frame="year",
    animation_group="country",
    size="pop",
    color="continent",
    hover_name="country",
    log_x=True,
    size_max=55,
    range_x=[100, 100000],
    range_y=[25, 90]
)

# fig["layout"].pop("updatemenus") # optional, drop animation buttons
fig.show()

"""

fig = px.line(death, x='Year', y='death', color='Entity')
fig.show()







inc = pd.read_csv('malaria_inc.csv')
inc.rename(columns={inc.columns[3]: "inc"}, errors='raise', inplace=True)
inc = inc.sort_values(by=['Year', 'inc'])
fig = go.Figure()
fig.add_trace(go.Bar(
    y=inc['Entity'],
    x=inc['inc'],
    orientation='h',
    marker=dict(
        color=inc['Year'],
    )
))
fig.update_layout(barmode='stack')
fig.show()

"""
