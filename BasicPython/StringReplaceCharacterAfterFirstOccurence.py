
# Write a Python program to get a string from a given string where all occurrences of its first char have been changed to '$',
# except the first char itself.
#Sample String : 'restart'
#Expected Result : 'resta$t'

#Method1
def replace(str):
    char = str[0]
    modifiedstr = str[1:].replace(char, "$")
    print(char + modifiedstr)

print(replace('restart'))

#Method2
#Using regex
from re import sub
s = 'restart'

print(sub(r"(?<!^)"+s[0], "$", s))

