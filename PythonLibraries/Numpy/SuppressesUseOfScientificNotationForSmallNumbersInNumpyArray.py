
# Write a Python program to suppresses the use of scientific notation for small numbers in numpy array.
#Expected Output:
#Original array elements:
#[ 1.60000000e-10 1.60000000e+00 1.20000000e+03 2.35000000e-01]
#Print array values with precision 3:
#[ 0. 1.6 1200. 0.235]

import numpy as np

a=[ 1.60000000e-10, 1.60000000e+00, 1.20000000e+03, 2.35000000e-01]

print(type(a))

array=np.asarray(a)
print(type(array))
print("Original Array Elements:")
print(array)

np.set_printoptions(suppress=True)
print(array)
