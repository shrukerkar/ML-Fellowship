
# Write a Python program to add, subtract, multiple and divide two Pandas Series.
# Sample Series: [2, 4, 6, 8, 10], [1, 3, 5, 7, 9]

import pandas as pd

df1=pd.Series([2, 4, 6, 8, 10])
df2=pd.Series([1, 3, 5, 7, 9])

df=df1+df2
print("Add Two Series:")
print(df)

df=df1*df2
print("Multiply Two Series:")
print(df)

df=df1-df2
print("Subtract Two Series:")
print(df)

df=df1/df2
print("Divide Two Series:")
print(df)
