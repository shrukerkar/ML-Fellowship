
#Build a machine learning model to predict profit of the company  based on different expenses for a given dataset
#https://drive.google.com/open?id=1dic5dbHugytxCO6i9pcD6RPod_sLkAUA


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import OneHotEncoder

#Read dataset
data=pd.read_csv("/home/shruti/Downloads/50_Startups.csv")
print(data.head())

#Slice dependent(y) and independent(X) variables
y=data.iloc[:,:-1]
print(y.shape)

X=data.iloc[:,:4]
print(X.shape)


#Plot dependent(y) and independent(X) variables
sns.regplot(x=data["Profit"],y=data["R&D Spend"])
plt.show()

sns.regplot(x=data["Profit"],y=data["Administration"])
plt.show()

sns.regplot(x=data["Profit"],y=data["Marketing Spend"])
plt.show()


#Encoding categorical variables
labelencoder_X=LabelEncoder()
X.values[:,3]=labelencoder_X.fit_transform(X.values[:,3])

#Onehotencoding
onehotencoder=OneHotEncoder(categorical_features=[3])
X=onehotencoder.fit_transform(X).toarray()

labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)


#Split dataset into trainset and testset
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Fit training data
regressor=LinearRegression()
print(regressor.fit(X_train,y_train))

#print coefficient of independent variables
print(regressor.coef_)

#print intercept for linear regression
print(regressor.intercept_)

#Prediction
y_pred=regressor.predict(X_test)

print(y_pred)

#R square score for dataset
print(regressor.score(X,y))



