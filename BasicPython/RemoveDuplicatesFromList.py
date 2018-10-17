
# Write a Python program to remove duplicates from a list.

list = [1, 2, 3, 1, 2, 5, 6, 7, 8]
duplicate_items=set()
items=[]
for i in list:
    if i not in duplicate_items:
        items.append(i)
        duplicate_items.add(i)
print(duplicate_items)
