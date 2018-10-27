
#Write a Python programming to display a bar chart of the popularity of programming Languages. Make blue border to each bar.
#Sample data:
#Programming languages: Java, Python, PHP, JavaScript, C#, C++
#Popularity: 22.2, 17.6, 8.8, 8, 7.7, 6.7

import matplotlib.pyplot as plt

programming_languages= ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8, 7.7, 6.7]

x=[i for i,_ in enumerate(programming_languages)]
y_pos=[0,1,4,7,9,10]

plt.bar(y_pos,popularity,color=[0.4,0.6,0.8,1.0],edgecolor='blue')

plt.xlabel("languages")
plt.ylabel("popularity")
plt.title("Popularity Of Programming Languages:")
plt.xticks(x,programming_languages)
plt.minorticks_on()
plt.grid(which='major',linestyle='-',linewidth='0.5',color='red')
plt.grid(which='minor',linestyle=':',linewidth='0.5',color='black')

plt.show()
