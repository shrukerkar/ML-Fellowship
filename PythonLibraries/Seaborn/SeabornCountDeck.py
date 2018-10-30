
#Write a program to draw a barplot to show count for a deck for a dataset given in the url
#https://github.com/mwaskom/seaborn-data/blob/master/titanic.csv

import matplotlib.pyplot as plt
import seaborn as sns

titanic=sns.load_dataset("titanic")

print(titanic)

x=sns.factorplot("class","survived","deck",data=titanic,kind="bar",size=6,palette="muted",legend=False)

x.set(yscale="log")

plt.show()
