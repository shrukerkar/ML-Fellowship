
#Write a Python program to generate all permutations of a list in Python.

import itertools

permutation_list=itertools.permutations([1,2,3])

#Returns result as a generator
print(permutation_list)

#Returns result as a list
print(list(permutation_list))
