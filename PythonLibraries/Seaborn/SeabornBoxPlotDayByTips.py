
#Write a program to draw a box plot of day by tips for a dataset given in a url
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv


import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset("tips")

print(tips)

x=sns.boxplot(x="day",y="tip",data=tips)

plt.show()


