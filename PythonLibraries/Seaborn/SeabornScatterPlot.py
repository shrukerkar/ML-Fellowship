
#Write a program to draw a scatter plot of “day” against “total bill” for a dataset given in a url
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

print(tips)

x=sns.scatterplot(x="total_bill",y="day",data=tips)

x.set(xlim=(0,100))

plt.show()