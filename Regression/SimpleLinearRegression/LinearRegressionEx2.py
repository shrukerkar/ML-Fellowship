
#Build a predictive linear regression model for given dataset, given humidity predict apparent temperature
#https://drive.google.com/open?id=1WsJxbsh51SL1UhT0xEvNynZTKy4nOwLM

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


df=pd.read_csv("/home/shruti/Downloads/weatherHistory.csv")
print(df.head())

print(df.describe(include=['O']))

print(df.corr())

data_set=df.iloc[:,[0,3,4,5,8]]
print(data_set.corr())

sns.regplot(x=data_set["Temperature (C)"],y=data_set["Humidity"])
plt.show()