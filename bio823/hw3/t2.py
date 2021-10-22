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



temp = df[df['entity']=='World'].copy()
print(temp)
df[df['entity']=='World'] =df[df['entity']=='Afghanistan']
df[df['entity']=='Afghanistan'] = temp


print(df[df['entity']=='World'])
print(

df[df['entity']=='Afghanistan'])