
# Write a Python program that accepts a comma separated sequence of words as input and
# prints the unique words in sorted form (alphanumerically).
#Sample Words : red, white, black, red, green, black
#Expected Result : black, green, red, white,red

string=input("Enter comma separated list of words:")

words=[word for word in string.split(",")]

print(",".join(sorted(list(set(words)))))
