import plotly.express as px
import pandas as pd

df = pd.read_csv("2022-09-11.log")

fig = px.scatter_geo(df,lat='latitude',lon='longitude', hover_name="source")
fig.update_layout(title = 'APRS map', title_x=0.5, geo_scope='usa')
fig.show()

#learn more - https://plotly.com/python/scatter-plots-on-maps/