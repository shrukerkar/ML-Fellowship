
# Write a Python program to how to add an extra column to an numpy array.
#Expected Output:
#[[ 10 20 30 100]
#[ 40 50 60 200]]

import numpy as np

x = np.array([[10,20,30], [40,50,60]])
y = np.array([[100], [200]])
print("Expected Output:")
print(np.append(x, y, axis=1))

