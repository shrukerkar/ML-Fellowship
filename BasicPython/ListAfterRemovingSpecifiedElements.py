
# Write a Python program to print a specified list after removing the 0th, 4th and 5th elements.

Sample_list=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
Expected_output = [x for (i,x) in enumerate(Sample_list) if i not in (0,4,5)]
print(Expected_output)