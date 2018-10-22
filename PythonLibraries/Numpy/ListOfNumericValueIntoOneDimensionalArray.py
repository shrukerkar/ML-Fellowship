
#Write a Python program to convert a list of numeric value into a one-dimensional NumPy array.
#Expected Output:
#Original List: [12.23, 13.32, 100, 36.32]
#One-dimensional numpy array: [ 12.23 13.32 100. 36.32]

import numpy as np

Original_list= [12.23, 13.32, 100, 36.32]

print(Original_list)

array= np.array(Original_list)

print(array)
print(type(array))
print(array.shape)