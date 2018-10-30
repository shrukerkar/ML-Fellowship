
#Write a program to draw a swarm plot of total bill against size  for a  given dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv

import seaborn as sns
import matplotlib.pyplot as plt

tips=sns.load_dataset("tips")

print(tips)

x=sns.swarmplot(x="size",y="total_bill",data=tips)

plt.show()