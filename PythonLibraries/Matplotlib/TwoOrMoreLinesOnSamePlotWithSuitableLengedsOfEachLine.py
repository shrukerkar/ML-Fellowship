
#Write a Python program to plot two or more lines on same plot with suitable legends of each line.


import matplotlib.pyplot as plt

x1=[30,40,50]
y1=[60,70,80]

plt.plot(x1,y1,label="line1")

x2=[10,20,90]
y2=[15,25,95]

plt.plot(x2,y2,label="line2")

plt.xlabel('x-axis')
plt.ylabel('y-axis')

plt.title('Two or more lines')

plt.legend()
plt.show()
