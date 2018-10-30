
#Write a program to draw a point plot for sex against survived for a dataset given in url
#https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

import seaborn as sns
import matplotlib.pyplot as plt


titanic=sns.load_dataset("titanic")

print(titanic)

x=sns.pointplot("sex","survived","class",data=titanic,kind="bar",size=6,palette="muted",legend=False)

x.set(yscale="log")

plt.show()

