
#Write a Python program to plot quantities which have an x and y position.

import matplotlib.pyplot as plt
import numpy as np

x1=range(1,40)

y1=[i*3 for i in x1]

x2=range(1,20)
y2=[i+2 for i in x2]


plt.axis([0,10,0,20])
plt.plot(x1,y1,'*b',x2,y2,'ro')
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample plot")
plt.show()