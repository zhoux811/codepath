import plotly.graph_objs as go
import pandas as pd
import numpy as np
import pandas as pd
import plotly as py
import plotly.graph_objects as go
import numpy as np
import plotly.express as px
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import datetime

df = pd.read_csv('malaria_deaths_age.csv')
print(df.head())
# print(death_age.describe())
"""
print('\n\n')

print(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)])
print(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)]['deaths'])
print(sum(death_age.loc[(death_age['entity'] == 'Afghanistan') & (death_age['year'] == 1991)]['deaths']))

print('\n\n')
"""
"""

# https://plotly.com/python/sliders/
fig = px.line(
    death_age,
    x="age_group",
    y="deaths",
    animation_frame="year",
    animation_group="entity",
    size="deaths",
    color="entity",
    hover_name="entity",
    # log_x=True,
    log_y=True,
    # size_max=55,
    # range_x=[100, 100000],
    # range_y=[25, 90]
)

# fig["layout"].pop("updatemenus") # optional, drop animation buttons
fig.show()
"""

"""
ages = df['age_group'].unique()
entites = df['entity'].unique()
print(df.columns)
print(ages)
print(entites)
"""

df.rename(columns={df.columns[3]: "num"}, errors='raise', inplace=True)
df.rename(columns={df.columns[1]: "label"}, errors='raise', inplace=True)
df.rename(columns={df.columns[4]: "color"}, errors='raise', inplace=True)
df.rename(columns={df.columns[5]: "value"}, errors='raise', inplace=True)
print(df.head())

df_input = df.copy()
############################################################


# split df by labels
dates = df['num'].unique().tolist()
labels = df['label'].unique().tolist()

# print(labels)
# print(dates)

# dataframe collection grouped by labels
dfs = {}
for label in labels:
    dfs[label] = pd.pivot_table(df[df['label'] == label],
                                values='value',
                                index=['num'],
                                columns=['color'],
                                aggfunc=np.sum)

# find row and column unions
common_cols = []
common_rows = []
for df in dfs.keys():
    common_cols = sorted(list(set().union(common_cols, list(dfs[df]))))
    common_rows = sorted(list(set().union(common_rows, list(dfs[df].index))))

# find dimensionally common dataframe
df_common = pd.DataFrame(np.nan, index=common_rows, columns=common_cols)

# reshape each dfs[df] into common dimensions
dfc = {}
for df_item in dfs:
    # print(dfs[unshaped])
    df1 = dfs[df_item].copy()
    s = df_common.combine_first(df1)
    df_reshaped = df1.reindex_like(s)
    dfc[df_item] = df_reshaped

# plotly start
fig = go.Figure()
# one trace for each column per dataframe: AI and RANDOM
for col in common_cols:
    fig.add_trace(go.Scatter(x=dates,
                             visible=True,
                             marker=dict(size=12, line=dict(width=2)),
                             marker_symbol='diamond', name=col
                             )
                  )

# menu setup
updatemenu = []

# buttons for menu 1, names
buttons = []

# create traces for each color:
# build argVals for buttons and create buttons
for df in dfc.keys():
    argList = []
    for col in dfc[df]:
        # print(dfc[df][col].values)
        argList.append(dfc[df][col].values)
    argVals = [{'y': argList}]

    buttons.append(dict(method='update',
                        label=df,
                        visible=True,
                        args=argVals))

# buttons for menu 2, colors
b2_labels = common_cols

# matrix to feed all visible arguments for all traces
# so that they can be shown or hidden by choice
b2_show = [list(b) for b in [e == 1 for e in np.eye(len(b2_labels))]]
buttons2 = []
buttons2.append({'method': 'update',
                 'label': 'All',
                 'args': [{'visible': [True] * len(common_cols)}]})

# create buttons to show or hide
for i in range(0, len(b2_labels)):
    buttons2.append(dict(method='update',
                         label=b2_labels[i],
                         args=[{'visible': b2_show[i]}]
                         )
                    )

# add option for button two to hide all
buttons2.append(dict(method='update',
                     label='None',
                     args=[{'visible': [False] * len(common_cols)}]
                     )
                )

# some adjustments to the updatemenus
updatemenu = []
your_menu = dict()
updatemenu.append(your_menu)
your_menu2 = dict()
updatemenu.append(your_menu2)
updatemenu[1]
updatemenu[0]['buttons'] = buttons
updatemenu[0]['direction'] = 'down'
updatemenu[0]['showactive'] = True
updatemenu[1]['buttons'] = buttons2
updatemenu[1]['y'] = 0.6
updatemenu[0]['x'] = -0.1
updatemenu[1]['x'] = -0.1

fig.update_layout(showlegend=True, updatemenus=updatemenu)
fig.update_layout(yaxis=dict(range=[0, df_input['value'].max() + 0.4]))

# button annotations
fig.update_layout(
    annotations=[
        dict(text="<i>Entity</i>", x=-0.4, xref="paper", y=1.1, yref="paper",
             align="left", showarrow=False, font=dict(size=16, color='steelblue')),
        dict(text="<i>Age_Group</i>", x=-0.4, xref="paper", y=0.7, yref="paper",
             align="left", showarrow=False, font=dict(size=16, color='steelblue')

             )
    ])

fig.show()

fig.write_html("v1.html")
