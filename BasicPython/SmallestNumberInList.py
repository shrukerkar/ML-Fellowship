
#Write a Python program to get the smallest number from a list.

def smallest_num(list):
    min=list[0]
    for i in list:
        if i<min:
            min=i
    return min
print(smallest_num([1,4,5,6,7,8]))