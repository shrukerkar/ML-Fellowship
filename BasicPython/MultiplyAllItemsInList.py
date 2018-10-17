
#Write a Python program to multiplies all the items in a list

def multiply(items):
    total=1
    for i in items:
        total*=i
    return total
print(multiply([1,2,3,4,5]))