
#Write a Python program to remove duplicates from a list of lists.

#Sample_list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
#New List : [[10, 20], [30, 56, 25], [33], [40]]

def remove_duplicate(sample_list):
    new_list = []
    for i in sample_list:
        if i not in new_list:
            new_list.append(i)
    return new_list

print(remove_duplicate([[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]))