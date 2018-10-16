
x=[[5,1,3],
   [1,1,1],
   [1,2,1]]

y=[1,2,3]


def matmul(m, v):
    rows = len(m)
    w = [0]*rows
    irange = range(len(v))
    sum = 0
    for j in range(rows):
        r = m[j]
        for i in irange:
            sum += r[i]*v[i]
        w[j],sum = sum,0
    return w
a=matmul([[5, 1, 3], [1, 1, 1], [1, 2, 1]], [1, 2, 3])
print(a)