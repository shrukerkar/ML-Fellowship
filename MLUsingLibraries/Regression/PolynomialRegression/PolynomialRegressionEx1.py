
# Build a machine learning model to predict salary  based on position for a given dataset
#https://drive.google.com/open?id=1jKfNxQkybZKprVpCkoL16mTjmSSnCol3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures


#Read Dataset.SDFJKL;'

data=pd.read_csv("/home/shruti/Downloads/Position_Salaries.csv")
print(data)

#Dependent(y) and independent(X) variables
X=data.iloc[:,1:2].values
print(X)

y=data.iloc[:,2].values
print(y)

##Split data into training and test set
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

#Fit traing data

linear_model=LinearRegression()
linear_model.fit(X,y)
predict=linear_model.predict(X)


polynomial_model=PolynomialFeatures(degree=4)
X_poly=polynomial_model.fit_transform(X)
print(X_poly)
polynomial_model.fit(X_poly,y)
linear_model2=LinearRegression()
linear_model2.fit(X_poly,y)
prediction=linear_model2.predict(X_poly)
plt.scatter(X,y,color='red')

#scatter plot
plt.scatter(X,predict,color='blue')
plt.title("Linear regression")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()

plt.scatter(X,y,color='blue')
plt.scatter(X,prediction,color='red')
plt.title("Polynomial Regression")
plt.xlabel("Position Level")
plt.ylabel("Salary")
plt.show()

print(linear_model.predict(6.5))

print(linear_model2.predict(polynomial_model.fit_transform(6.5)))