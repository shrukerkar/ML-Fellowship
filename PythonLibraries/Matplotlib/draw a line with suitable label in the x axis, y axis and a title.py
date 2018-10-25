
# Write a Python program to draw a line with suitable label in the x axis, y axis and a title

import matplotlib.pyplot as plt

x=[5,8,10]
y=[12,11,13]

plt.plot(x,y,linewidth=5)

plt.title("Sample Plot")
plt.xlabel("Something on x axis")
plt.ylabel("Something on y axis")
plt.show()