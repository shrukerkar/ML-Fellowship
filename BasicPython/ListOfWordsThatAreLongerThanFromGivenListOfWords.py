
#Write a Python program to find the list of words that are longer than n from a given list of words

#Method 1
a=[]
n=int(input("Enter the number of elements in list of words:"))
# Loop for appending element to list a
for x in range(0,n):
    element = input("Enter element" + str(x + 1) + ":")
    a.append(element)

max = len(a[0])
temp_var = a[0]

#Check input list of words are greater than max
for i in a:
    if (len(i) > max):
        max = len(i)
        emp = i
print("The word with the longest length is:")
print(temp_var)

#Method 2

def words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len
print(words(3, " How was your day"))
