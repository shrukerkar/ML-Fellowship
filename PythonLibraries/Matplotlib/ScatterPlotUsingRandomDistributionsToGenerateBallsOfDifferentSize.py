
#Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes
import math
import random

import matplotlib.pyplot as plt
import numpy as np

num_empty_circles=20

x=[random.triangular() for i in range (num_empty_circles)]
y=[random.gauss(0.5,0.25) for i in range (num_empty_circles)]
color=[random.randint(1,4) for i in range (num_empty_circles)]
areas=[math.pi * random.randint(5, 15) ** 2 for i in range(num_empty_circles)]
plt.figure()
plt.scatter(x,y,c=color,s=areas,alpha=0.85)
plt.axis([0.0, 1.0, 0.0, 1.0])
plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')
plt.show()