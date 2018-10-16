

def group_member(group_data, n):
    for value in group_data:
        if n == value:
            return True
    return False
print(group_member([1, 5, 8, 3], 3))
print(group_member([1,5,8,3],-1))
