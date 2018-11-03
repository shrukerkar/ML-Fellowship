
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
sns.regplot(x=data_set["Temperature (C)"], y=data_set["Apparent Temperature (C)"])
plt.show()

#Remove Outliers in dataset

outliers=[]
def dect_outlier(data):
    limit=3
    mean=np.mean(data)
    std=np.std(data)
    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>limit:
            outliers.append(i)
    return outliers
outlier_data=dect_outlier(data_set["Humidity"])
print(outlier_data)

final_data_set=data_set[data_set["Humidity"]>0.15]
print(final_data_set)

sns.regplot(x=final_data_set["Temperature (C)"],y=final_data_set["Humidity"])
plt.show()


final_data_set=data_set[data_set["Humidity"]<=0.15]
print(final_data_set)