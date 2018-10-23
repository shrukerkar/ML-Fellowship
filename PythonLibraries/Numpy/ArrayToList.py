
#Write a Python program to convert a NumPy array into Python list structure.
#Expected Output:
#Original array elements:
#[ 0.26153123 0.52760141 0.5718299 0.5927067 0.7831874 0.69746349
#0.35399976 0.99469633 0.0694458 0.54711478]
#Print array values with precision 3:
#[ 0.262 0.528 0.572 0.593 0.783 0.697 0.354 0.995 0.069 0.547]

import numpy as np

a= [ 0.26153123, 0.52760141, 0.5718299, 0.5927067, 0.7831874, 0.69746349,
     0.35399976, 0.99469633, 0.0694458, 0.54711478]

print(type(a))

array=np.asarray(a)
print("Original Array Elements:")
print(array)
print(type(array))

np.set_printoptions(precision=3)
print("Print Array Values With Precision 3:")
print(array)


