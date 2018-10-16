from collections import defaultdict,Counter

str='shruti'
dict={}

for letter in str:
    dict[letter]=dict.get(letter,0)+1
print(dict)