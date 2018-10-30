
#Write a program to draw box plot of life expectancy by continent for a data set given in a url
#  https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data_url= "https://raw.githubusercontent.com/resbaz/r-novice-gapminder-files/master/data/gapminder-FiveYearData.csv"

df=pd.read_csv(data_url)

print(df.head())

x=sns.boxplot(x="continent",y="lifeExp",data=df)

plt.show()