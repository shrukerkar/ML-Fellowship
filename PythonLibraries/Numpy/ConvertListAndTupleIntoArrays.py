
#Write a Python program to convert a list and tuple into arrays.
#List to array:
#[1 2 3 4 5 6 7 8]
#Tuple to array:
#[[8 4 6]
#[1 2 3]]

import numpy as np

list = [1, 2, 3, 4, 5, 6, 7, 8]
print("List to array: ")
print(np.asarray(list))
tuple = ([8, 4, 6], [1, 2, 3])
print("Tuple to array: ")
print(np.asarray(tuple))

