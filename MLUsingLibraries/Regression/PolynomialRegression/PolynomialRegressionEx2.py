
# For a given dataset predict number of bikes getting shared based on different parameters
#https://drive.google.com/open?id=1ohN2o3zSZ2Xuy4CIdTWN-dTmciUXizst

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

#Read dataset

data=pd.read_csv("/home/shruti/Downloads/bike_sharing.csv",index_col="instant",parse_dates=True)
print(data.head())
print(data.corr())

data.rename(columns={'cnt':'total'},inplace=True)

#Visualizing dataset

data.plot(kind='scatter',x='temp',y='total',alpha=0.2)
plt.show()

sns.lmplot(x='temp',y='total',data=data,aspect=1.5,scatter_kws={'alpha':0.2})
plt.show()

#Dependent(y) and independent(X) variables

feature_col=['temp']
X=data[feature_col]
print(X.shape)
y=data.total
print(y.shape)


#Split data into training and test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train.shape)
print(X_test.shape)
print(y_train.shape)
print(y_test.shape)

#Fit traing data

regressor=LinearRegression()
print(regressor.fit(X_train,y_train))

y_pred=regressor.predict(X_test)
print(y_pred)

polynomial_model=PolynomialFeatures(degree=4)
X_poly=polynomial_model.fit_transform(X_train)
print(X_poly)

polynomial_model.fit(X_poly,y_train)

linear_model2=LinearRegression()
linear_model2.fit(X_poly,y_train)

prediction=linear_model2.predict(X_poly)

plt.scatter(X_train,y_train,color='red')
plt.scatter(X,y_pred,color='blue')
plt.title("Linear regression")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.scatter(X_train,y_test,color='blue')
plt.scatter(X,prediction,color='red')
plt.title("Polynomial Regression")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()




