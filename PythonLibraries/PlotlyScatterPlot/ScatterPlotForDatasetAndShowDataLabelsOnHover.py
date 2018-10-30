
#Write a program to draw a scatter plot for a given dataset and show datalabels on hover
#https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np
import pandas as pd

plotly.tools.set_credentials_file(username='shrukerkar',api_key='Xz0m9hmG79qoKrR9kam6')
l=[]
y=[]
data_url="https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv"

df=pd.read_csv(data_url)
print(df)

N=50

for i in range(int(N)):
    y.append((2000+i))
    trace0=go.Scatter(x=df['Rank'],y=df['Population']+(i*1000000),mode='markers',marker=dict(size=14,line=dict(width=1),color='rgba(152, 0, 0, .8)',opacity=0.3),name= y[i],
        text= df['State']) # The hover text goes here...
    l.append(trace0);

layout= go.Layout(
    title= 'Stats of USA States',
    hovermode= 'closest',
    xaxis= dict(
        title= 'Population',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2, ),
    yaxis=dict(
        title= 'Rank',
        ticklen= 5,
        gridwidth= 2,
    ),
    showlegend= False
)
fig= go.Figure(data=l, layout=layout)
py.plot(fig)
