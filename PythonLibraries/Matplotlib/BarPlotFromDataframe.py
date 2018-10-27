
# Write a Python program to create bar plot from a DataFrame.
#Sample Data Frame:
#a b c d e
#2 4,8,5,7,6
#4 2,3,4,2,6
#6 4,7,4,7,8
#8 2,6,4,8,6
#10 2,4,3,3,2

import matplotlib.pyplot as plt
from pandas import DataFrame
import numpy as np


x=np.array([[4,5,6,7],[1,2,3,8],[4,2,5,6],[8,9,4,5]])
df= DataFrame(x, columns=['a', 'b', 'c', 'd'], index=[2, 4, 6, 8])

df.plot(kind='bar')

plt.minorticks_on()
plt.grid(which='major',linestyle='- ',linewidth='0.5',clor='green')
plt.grid(which='major',linestyle=':',linewidth='0.5',clor='red')

plt.show()