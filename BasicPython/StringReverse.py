
#Write a Python program to reverse a string.

#Method 1

def reverse(str):
    str=""
    for i in str:
        str=i+str
    return str

str="we3resource"

print("The original string  is : ", end="")
print(str)

print("The reversed string(using loops) is : ", end="")
print(reverse(str ))

#Method 2

def reverse(s):
    if len(s) == 0:
        return s
    else:
        return reverse(s[1:]) + s[0]


s = "we3resource"

print("The original string  is : ", end="")
print(s)

print("The reversed string(using recursion) is : ", end="")
print(reverse(s))

#Method 3

def reverse(string):
    string = "".join(reversed(string))
    return string


string = "we3resource"

print("The original string  is : ", end="")
print(string)

print("The reversed string(using reversed) is : ", end="")
print(reverse(string))