import pandas as pd


def check(file, country):
    df = pd.read_csv(file)
    data_country = df.loc[df["Country/Region"] == country]
    
    total_days = len(p.columns) - 4
    x_data = data_country.columns[4:]

    y_data = [data_country[date].values[0] for date in dates]


    return x_data, y_data, data_country


x_confirmed, y_confirmed, confirmed_data = check("time_series_19-covid-Confirmed.csv", "India")
x_recovered, y_recovered, recovered_data = check("time_series_19-covid-Recovered.csv", "India")


import plotly.graph_objects as go


fig = go.Figure()


                
 
fig.add_trace(go.Scatter(x=x_confirmed, y=y_confirmed, name="Confirmed Cases",
                line_color='deepskyblue',
                opacity=0.8))


fig.add_trace(go.Scatter(x=x_confirmed ,y=y_recovered, name="Recovered Cases",
                line_color='dimgray',
                opacity=0.8))


fig.update_layout(title_text='COVID-19 impact - India')
fig.show()
