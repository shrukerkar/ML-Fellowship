
# Write a Python program to find the set difference of two arrays. The set difference will return the sorted, unique values in array1 that are not in array2.
#Expected Output:
#Array1: [ 0 10 20 40 60 80]
#Array2: [10, 30, 40, 50, 70, 90]
#Set difference between two arrays:
#[ 0 20 60 80]

import numpy as np

array1=np.array([ 0, 10, 20, 40, 60, 80])

array2= [10, 30, 40, 50, 70, 90]

array=(np.setdiff1d(array1,array2))

print("Set difference between two arrays:",array)