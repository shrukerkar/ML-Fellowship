
#Write a Python program to add a border (filled with 0's) around an existing array.
#Expected Output:
#Original array:
#[[ 1. 1. 1.]
#[ 1. 1. 1.]
#[ 1. 1. 1.]]
#1 on the border and 0 inside in the array
#[[ 0. 0. 0. 0. 0.]
#[ 0. 1. 1. 1. 0.]
#[ 0. 1. 1. 1. 0.]
#[ 0. 1. 1. 1. 0.]
#[ 0. 0. 0. 0. 0.]]

import numpy as np

x=np.ones((3,3))
print(x)

x=np.pad(x,pad_width=1,mode='constant',constant_values=0)
print(x)
