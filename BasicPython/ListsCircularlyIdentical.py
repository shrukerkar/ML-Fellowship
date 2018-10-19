
#Write a python program to check whether two lists are circularly identical.

list1=[1,1,1,0,0]
list2=[1,1,0,0,1]



print(''.join(map(str,list2)) in ''.join(map(str,list1*2)))

