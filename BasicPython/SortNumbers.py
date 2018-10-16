
a = int(input("Input first number: "))
b = int(input("Input second number: "))
c = int(input("Input third number: "))

a1 = min(a, b, c)
a3 = max(a, b, c)
a2 = (a + b + c) - a1 - a3
print("Numbers in sorted order: ", a1, a2, a3)
