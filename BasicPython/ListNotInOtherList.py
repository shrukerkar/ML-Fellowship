
list_1 = set(["White", "Black", "Red"])
list_2 = set(["Red", "Green"])
new_list=[]
for color in list_1:
   if color not in list_2:
     new_list.append(color)
new_list=set(new_list)
print (new_list)
