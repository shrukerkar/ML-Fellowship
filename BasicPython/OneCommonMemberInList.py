
#Write a Python function that takes two lists and returns True if they have at least one common member.

#Method1

a=input("Enter number of items in list a:")
b=input("Enter number of items in list b:")

for i in a:
    for j in b:
        if i == j:
           print( "result:", True)
    else:
        print("result:",False)

#Method2
def overlap(a,b):
    for i in a:
        for j in b:
            return i==j
print("Result is:",overlap([1,2,4,5,6],[5,6,7,8,9 ]))