
#Write a Python program to find common values between two arrays.
#Expected Output:
#Array1: [ 0 10 20 40 60]
#Array2: [10, 30, 40]
#Common values between two arrays:
#[10 40]

import numpy as np

array1=[10, 20, 40, 60]
array2=[10, 30, 40]
array=np.intersect1d(array1,array2)
print("Common values between two arrays:",array)