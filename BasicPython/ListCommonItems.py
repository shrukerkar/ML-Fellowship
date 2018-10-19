
# Write a Python program to find common items from two lists.

#Method1

def common_elements(list1, list2):
    result = []
    for element in list1:
        if element in list2:
            result.append(element)
    return result
print(common_elements([1,2,3,4,5],[5,4,3,6,7]))

#Method2

list1=[1,2,3,4,5]
list2=[5,4,3,6,7]

print(list(set(list1).intersection(list2)))