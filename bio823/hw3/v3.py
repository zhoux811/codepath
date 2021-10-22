import plotly as py
import plotly.graph_objects as go
import numpy as np
import pandas as pd
import plotly.express as px

inc = pd.read_csv('malaria_inc.csv')
inc.rename(columns={inc.columns[3]: "inc"}, errors='raise', inplace=True)
inc = inc.sort_values(by=['Year', 'inc'])

"""

fig = go.Figure()
fig.add_trace(go.Bar(
    y=inc['Entity'],
    x=inc['inc'],
    orientation='h',
    marker=dict(
        color=inc['Year'],
    )
))
#fig.update_layout(barmode='stack')
fig.show()
"""



inc['Year'] = inc['Year'].astype(str)

fig = px.bar(
    inc,
    y='Entity',
    x='inc',
    orientation='h',
    color='Year',
    color_continuous_scale=px.colors.sequential.PuBu,
)
fig.show()

fig.write_html("v3.html")
