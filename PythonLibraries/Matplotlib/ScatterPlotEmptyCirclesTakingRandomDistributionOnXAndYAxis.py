
#Write a Python program to draw a scatter plot using random distributions to generate balls of different sizes.
import random

import matplotlib.pyplot as plt
import numpy as np
x = np.random.randn(50)
y = np.random.randn(50)
plt.scatter(x, y, s=70, facecolors='none', edgecolors='g')


plt.xlabel('x axis')
plt.ylabel('y axis')
plt.title('scatter plot')
plt.show()

