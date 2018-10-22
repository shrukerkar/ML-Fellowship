
#Write a Python program to save a NumPy array to a text file.

import numpy as np

a=np.arange(1.0,2.0,3.0)
np.savetxt('file.out',a,delimiter=',')
