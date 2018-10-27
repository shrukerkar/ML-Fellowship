
#Write a Python program to create bar plots with error bars on the same figure. Sample Date
#Mean velocity: 0.2474, 0.1235, 0.1737, 0.1824
#Standard deviation of velocity: 0.3314, 0.2278, 0.2836, 0.2645

import matplotlib.pyplot as plt
import numpy as np

N=5
mean=(54.74, 42.35, 67.37, 58.24, 30.25)
std=(4, 3, 4, 1, 5)

index=np.arange(N)
width=0.35
plt.bar(index,mean,width,yerr=std,color='red')
plt.ylabel('scores')
plt.xlabel('velocity')
plt.title('Score & Velocity')

plt.minorticks_on()
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()