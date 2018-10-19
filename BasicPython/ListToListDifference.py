
# Write a Python program to get the difference between the two lists.

list1=[1,2]
list2=[2,3]

Diffrence=set(list1) - set(list2)
print(Diffrence)
print(list(Diffrence))
Symmetric_Diffrence=set(list1).symmetric_difference(set(list2))
print(Symmetric_Diffrence)
print(list(Symmetric_Diffrence))