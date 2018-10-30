
#Write a program to draw swarm plot of “total bill” against day for a dataset given in url
#https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv


import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

print(tips)

x=sns.swarmplot(x="day",y="total_bill",data=tips)

plt.show()