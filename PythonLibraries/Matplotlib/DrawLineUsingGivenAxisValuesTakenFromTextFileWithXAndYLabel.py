
#Write a Python program to draw a line using given axis values taken from a text file, with suitable label in the x axis, y axis and a title.
#Test Data:
#test.txt
#1 2
#2 4
#3 1


import matplotlib.pyplot as plt

with open("/home/shruti/test.txt") as f:
    data = f.read()
data=data.split('\n')

x = [row.split(' ')[0] for row in data]
y = [row.split(' ')[1] for row in data]
plt.plot(x, y)

plt.title('Sample plot')
plt.xlabel('Something On X-axis')
plt.ylabel('Something On Y-axis')
plt.show()






