
#Write a program to draw a violin plot of sex against day  for a  given dataset
# https://raw.githubusercontent.com/mwaskom/seaborn-data/master/tips.csv
import seaborn as sns
import matplotlib.pyplot as plt


tips=sns.load_dataset("tips")
print(tips)

x=sns.violinplot(x="day",y="total_bill",hue="sex",data=tips,split=True,scale="count")


plt.show()



