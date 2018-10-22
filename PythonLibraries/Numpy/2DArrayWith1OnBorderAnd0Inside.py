
#Write a Python program to create a 2d array with 1 on the border and 0 inside.
#Expected Output:
#Original array:
#[[ 1. 1. 1. 1. 1.]
#[ 1. 1. 1. 1. 1.]
#[ 1. 1. 1. 1. 1.]
#[ 1. 1. 1. 1. 1.]
#[ 1. 1. 1. 1. 1.]]
#1 on the border and 0 inside in the array
#[[ 1. 1. 1. 1. 1.]
#[ 1. 0. 0. 0. 1.]
#[ 1. 0. 0. 0. 1.]
#[ 1. 0. 0. 0. 1.]
#[ 1. 1. 1. 1. 1.]]

import numpy as np

x=np.ones((5,5))
print(x)

x[1:-1,1:-1]=0

print(x)