
#Write a Python program to create a null vector of size 10 and update sixth value to 11.
#[ 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
#Update sixth value to 11
#[ 0. 0. 0. 0. 0. 0. 11. 0. 0. 0.]

import numpy as np

x=np.zeros(10)

print(x)

x[6]=11

print(x)

