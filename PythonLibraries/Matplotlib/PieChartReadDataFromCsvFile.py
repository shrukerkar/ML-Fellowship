
#Write a Python programming to create a pie chart of gold medal achievements of five most successful countries in 2016 Summer Olympics. Read the data from a csv file.
#Sample data:
#medal.csv
#country,gold_medal
#United States,46
#Great Britain,27
#China,26
#Russia,19
#Germany,17

import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("/home/shruti/medal.csv")
print(df)

country=df['country']
print(country)

medal=df['gold_medal']
print(medal)

color=['red', 'gold', 'yellowgreen', 'blue', 'lightcoral', 'lightskyblue']

explode =(0.1,0,0,0,0)


plt.pie(medal, explode=explode, labels=country  , colors=color,autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Medal achievements of five most successful countries in 2016 Summer Olympics ",bbox={'facecolor':'0.8','pad':5})

plt.show()