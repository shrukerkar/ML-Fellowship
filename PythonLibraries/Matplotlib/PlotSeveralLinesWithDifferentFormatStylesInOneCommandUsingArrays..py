
#Write a Python program to plot several lines with different format styles in one command using arrays

import matplotlib.pyplot as plt
import numpy as np

x=np.arange(0.,5.0,0.2)

plt.plot(x,x,'g--',x,x**2,'bs',x,x**3,'r^')
plt.show()