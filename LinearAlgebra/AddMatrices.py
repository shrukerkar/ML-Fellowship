

x=[[12,7,3],
   [4,5,6],
   [7,8,9]]

y=[[5,8,1],
   [6,7,3],
   [4,5,9]]

result = [map(sum, zip(*i)) for i in zip(x, y)]

print(result)
