
# Write a Python program to get the last part of a string before a specified character.
#https://www.w3resource.com/python-exercises
#https://www.w3resource.com/python

x='https://www.w3resource.com/python-exercises'
y='https://www.w3resource.com/python'

print (x.rsplit('-',1)[0])
print(y.rsplit('/',1)[0])

