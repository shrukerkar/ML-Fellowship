
#Write a program to draw a violin plot of “species” against “sepal length” for a dataset given in a url
#https://github.com/mwaskom/seaborn-data/blob/master/iris.csv


import seaborn as sns
import matplotlib.pyplot as plt

iris=sns.load_dataset("iris")

print(iris)

x=sns.violinplot(x="species",y="sepal_length",data=iris)

plt.show()