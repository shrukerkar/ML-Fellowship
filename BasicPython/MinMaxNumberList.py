list = []
num = int(input('numbers: '))

for n in range(num):
    numbers = int(input('Enter number: '))
    list.append(numbers)

print("Maximum element in the list :", max(list), "\nMinimum element in the list:", min(list))
