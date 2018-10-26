
# Write a Python program to display the current axis limits values and set new axis values.


import matplotlib.pyplot as plt

x=range(1,40)

y=[i*3 for i in x]

plt.plot(x,y)
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Sample plot")

print(plt.axis())

plt.axis([0,20,30,40])

plt.show()