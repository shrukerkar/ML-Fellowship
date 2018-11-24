
# Build a machine learning model to predict salary  based on position for a given dataset
#https://drive.google.com/open?id=1jKfNxQkybZKprVpCkoL16mTjmSSnCol3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVR

#Read dataset

data=pd.read_csv("/home/shruti/Downloads/Position_Salaries.csv")
print(data.head())

#Dependent(y) and independent(X) variables

X=data.iloc[:,1:2].values
print(X)

y=data.iloc[:,2].values
print(y)

#Split data into training set and test set
#X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20,random_state=0)
#print(X_train)
#print(X_test)
#print(y_train)
#print(y_test)

#Feature Scaling
sc_X=StandardScaler()
print(sc_X)
X=sc_X.fit_transform(X)
print(X)
sc_y=StandardScaler()
y=sc_y.fit_transform(y)
print(y)

regressor=SVR(kernel='rbf')
regressor.fit(X,y)

y_pred=regressor.predict(6.5)

plt.scatter(X,y,color='red')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('SVR')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()







