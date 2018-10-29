
# Write a Python programming to create a pie chart with a title of the popularity of programming Languages.Make multiple wedges of the pie.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

languages=['Java', 'Python', 'PHP', 'JavaScript','C#','C++']
popularity = [22.2,17.6,8.8,8,7.7,6.7]

color=['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']

explode =(0.1, 0, 0, 0,0,0)

plt.pie(popularity, explode=explode, labels=languages, colors=color,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Popularity of programming languages",bbox={'facecolor':'0.8','pad':5})

plt.show()