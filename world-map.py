
"""
Author : Prateek Chanda
"""

import pandas as pd
import numpy as np

conf = pd.read_csv("time_series_19-covid-Confirmed.csv")

unique_country = list(set(conf["Country/Region"].values))

q = conf.loc[conf["Country/Region"] == unique_country[0]].T
country_df = q.ix[:4].T
dates = (data_country.columns[4:])
col = q.ix[4:].columns[0]
dat = {'Date' : dates, 'Cases' : q.ix[4:][col]  }
new_df = pd.DataFrame (dat, columns = ['Date','Cases'])
l = cartesian(new_df, country_df)


for country_name in unique_country[1:]:
    #print (country_name)
    q = conf.loc[conf["Country/Region"] == country_name].T
    country_df = q.ix[:4].T
    dates = (data_country.columns[4:])
    col = q.ix[4:].columns[0]
    dat = {'Date' : dates, 'Cases' : q.ix[4:][col]  }
    new_df = pd.DataFrame (dat, columns = ['Date','Cases'])
    result = cartesian(new_df, country_df)
    l = l.append(result, ignore_index=True)
    
    
    
import plotly.express as px
df = px.data.gapminder()
fig = px.scatter_geo(l, lon=l["Long"], lat=l["Lat"], color="Country/Region",
                     hover_name="Country/Region", size="Cases",
                     animation_frame="Date",
                     projection="natural earth")
fig.show()
