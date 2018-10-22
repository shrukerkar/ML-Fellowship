
# Write a Python program to create a contiguous flattened array.
#Original array:
#[[10 20 30]
#[20 40 50]]
#New flattened array:
#[10 20 30 20 40 50]

import numpy as np

x=np.array([[10, 20, 30],[20, 40, 50]])

y=np.ravel(x)

print("New flattened array:",y)
