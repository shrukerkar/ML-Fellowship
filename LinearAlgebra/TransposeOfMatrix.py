
x=[[12,7,3],
   [4,5,6],
   [7,8,9]]

result=[[0,0,0],
        [0,0,0],
        [0,0,0]]

for i in range(len(x)):
    for j in range(len(x[0])):
        result[j][i]=[i][j]
for r in result:
    print(r)