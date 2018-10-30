

#Write a program to draw a scatter plot for random 1000 x and y coordinates

import plotly.plotly as py
import plotly.graph_objs as go
import numpy as np

N=1000

x_random=np.random.randn(N)
y_random=np.random.randn(N)

trace=go.Scatter(x=x_random,y=y_random,mode='markers')

data = [trace]

py.plot(data, filename='basic-line')