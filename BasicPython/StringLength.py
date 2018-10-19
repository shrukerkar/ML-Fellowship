
#Write a Python program to calculate the length of a string

#Method1
str = input("Enter a string:")

count=0

for i in str:
    count=count+1
print("Length of input string is:",count)

#Method2

str1 = input("Enter a string:")

print("Length of input string is:",len(str1))