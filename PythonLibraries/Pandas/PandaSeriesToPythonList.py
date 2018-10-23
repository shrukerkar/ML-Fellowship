
# Write a Python program to convert a Panda module Series to Python list and it's type.

import pandas as pd

df=pd.Series([10,24,30,25,40])
print(df)
print(type(df))

print("Python list:")
print(df.tolist())

