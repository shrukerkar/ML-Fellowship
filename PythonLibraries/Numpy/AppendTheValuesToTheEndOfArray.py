
#Write a Python program to append values to the end of an array.
#Expected Output:
#Original array:
#[10, 20, 30]

import numpy as np

x=[10, 20, 30]
print(x)
print(type(x))
x=np.append(x,[[40,50,60],[70,80,90]])

print(x)

print(type(x))