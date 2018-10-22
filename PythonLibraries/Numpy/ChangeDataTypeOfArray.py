
# Write a Python program to change the data type of an array.
#Expected Output:
#[[ 2 4 6]
#[ 6 8 10]]
#Data type of the array x is: int32
#New Type: float64
#[[ 2. 4. 6.]
#[ 6. 8. 10.]]

import numpy as np

x=np.array([[2,4,6],[6,8,10]])
print(x)
print("Data Type of the array x is:",x.dtype)

y=x.astype(float)

print("New Type:",y)