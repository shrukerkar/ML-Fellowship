
# Write a Python programming to display a horizontal bar chart of the popularity of programming Languages.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7


import matplotlib.pyplot as plt
import numpy as np

x=np.random.seed(30)

plt.rcdefaults()
fig,ax=plt.subplots()


programming_languages= ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
y_pos=np.arange(len(programming_languages))
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]
error=np.random.rand(len(programming_languages))

ax.barh(y_pos,popularity,xerr=error,align='center',color='green',ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(popularity)
ax.invert_yaxis()

ax.set_xlabel('popularity')
ax.set_title('BarChartHorizontal')
plt.show()


