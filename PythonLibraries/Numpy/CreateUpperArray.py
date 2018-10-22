
# Write a Python program to create an array which looks like below array.
#Expected Output:
#[[ 0. 0. 0.]
#[ 1. 0. 0.]
#[ 1. 1. 0.]
#[ 1.,1.,1.]

import numpy as np

print(np.tril(np.ones((4,4),dtype=int),-1))

