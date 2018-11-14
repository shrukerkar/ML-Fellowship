
#Build a machine learning model to predict profit of the company  based on different expenses for a given dataset
#https://drive.google.com/open?id=1dic5dbHugytxCO6i9pcD6RPod_sLkAUA


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns


data=pd.read_csv("/home/shruti/Downloads/50_Startups.csv")
print(data.head())
print(data.isnull)

sns.regplot(x=data["Profit"],y=data["R&D Spend"])
plt.show()

sns.regplot(x=data["Profit"],y=data["Administration"])
plt.show()

sns.regplot(x=data["Profit"],y=data["Marketing Spend"])
plt.show()

y=data.iloc[:,[4]]
print(y.shape)

X=data.iloc[:,[0,1,2]]
print(X.shape)


X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

regressor=LinearRegression()
print(regressor.fit(X_train,y_train))

print(regressor.coef_)

print(regressor.intercept_)

y_pred=regressor.predict(X_test)

print(y_pred)

print(regressor.score(X,y))
