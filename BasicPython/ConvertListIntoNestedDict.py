
list = [1, 2, 3, 4]
dict = current = {}
for name in list:
    current[name] = {}
    current = current[name]
print(dict)
