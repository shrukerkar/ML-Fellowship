
# Write a Python program to remove specific elements in a numpy array.
#Expected Output:
#Original array:
#[ 10 20 30 40 50 60 70 80 90 100]
#Delete first, fourth and fifth elements:
#[ 20 30 60 70 80 90 100]


import numpy as np
a=np.array([ 10, 20, 30, 40, 50, 60, 70, 80, 90, 100])

print("Original Array:")
print(a)

b=np.delete(a,[0,3,4])
print("Delete first,fourth and fifth elements:")
print(b)