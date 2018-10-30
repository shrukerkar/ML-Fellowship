
# Write a program to draw line and scatter plots for random 100 x and y coordinates

import plotly
import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np


plotly.tools.set_credentials_file(username='shrukerkar',api_key='Xz0m9hmG79qoKrR9kam6')

N=100

x_random=np.linspace(0,1,N)

y0_random=np.random.randn(N)+5
y1_random=np.random.randn(N)
y2_random=np.random.randn(N)-5

trace0=go.Scatter(x=x_random,y=y0_random,mode='markers',name='markers')

trace1=go.Scatter(x=x_random,y=y1_random,mode='lines+markers',name='lines+markers')

trace2=go.Scatter(x=x_random,y=y2_random,mode='lines',name='lines')

data=[trace0,trace1,trace2]

py.plot(data,filename='scatter-mode')