
#Write a Python program to count occurrences of a substring in a string.


#Method 1
str = 'The quick brown fox jumps over the lazy dog.'
str1='Hello fox'
print(str)
print(str.count("fox"))

#Method 2

print(len(str.split(str1))-1)