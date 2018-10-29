
#Write a Python program to draw a scatter graph taking a random distribution in X and Y and plotted against each other.

import matplotlib.pyplot as plt

import numpy as np

x=np.random.rand(10)
y=np.random.rand(10)

plt.scatter(x,y)
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')
plt.show()