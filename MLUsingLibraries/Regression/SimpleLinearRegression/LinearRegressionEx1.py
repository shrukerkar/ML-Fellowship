
#Build a machine learning model to predict salary based on experience for a given dataset
#https://drive.google.com/open?id=1UAbkc53H9fpJiEKCUICw1kXsrCdc0uU1

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import seaborn as sns
from sklearn.linear_model import LinearRegression
from sklearn import metrics
import math
import statsmodels.api as sm



#Read data set check correlation

data=pd.read_csv("/home/shruti/Downloads/Salary_Data.csv")
print(data.head())
print(data.shape)
print(data.corr())
#Plot dataset
sns.regplot(x=data["YearsExperience"],y=data["Salary"])
plt.show()
# Slice dependent(y) and independent variables(X)
y=data.iloc[:,[0]]
print(y)

X=data.iloc[:,[1]]
print(X)

#Split data set into train set and test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)

print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Fit training data
regressor=LinearRegression()
regressor.fit(X_train,y_train)

#print coefficients of independent variables

print(regressor.coef_)

#print intercept for linear regression

print(regressor.intercept_)

#prediction

y_pred=regressor.predict(X_test)

print(y_pred)

# R square for dataset

print(regressor.score(X,y))

#RMSE error

print(math.sqrt(metrics.mean_squared_error(y_test,y_pred)))

#Ordinary least sqaure method to fit regression line

ones_1=[1]*X.count()
X["b0"]=ones_1

model=sm.OLS(y_pred,X_test).fit()
print(model.summary())

# Scatter plot
plt.scatter(X_test, y_test, label='Dataset')
plt.plot(X_test, y_pred, label='predicted value')
plt.legend()
plt.show()
