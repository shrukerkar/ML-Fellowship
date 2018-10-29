
#Write a program to draw bar plot of sex against survived for a dataset given in the url
#https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

import seaborn as sns
import matplotlib.pyplot as plt


titanic=sns.load_dataset("titanic")

print(titanic)

x=sns.factorplot("class","survived","sex",data=titanic,kind="bar",size=6,palette="muted",legend=False)
x.set(yscale="log")
plt.show()


