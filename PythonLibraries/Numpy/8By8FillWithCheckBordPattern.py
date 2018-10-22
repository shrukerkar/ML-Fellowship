
# Write a Python program to create a 8x8 matrix and fill it with a checkerboard pattern.
#Checkerboard pattern:
#[[0 1 0 1 0 1 0 1]
#[1 0 1 0 1 0 1 0]
#[0 1 0 1 0 1 0 1]
#[1 0 1 0 1 0 1 0]
#[0 1 0 1 0 1 0 1]
#[1 0 1 0 1 0 1 0]
#[0 1 0 1 0 1 0 1]
#[1 0 1 0 1 0 1 0]]

import numpy as np

x=np.ones((3,3))
print(x)
x=np.zeros((8,8),dtype=int)
print(x)
x[1::2,::2]=1
x[::2,1::2]=1
print("CheckBoardPattern:",x)
