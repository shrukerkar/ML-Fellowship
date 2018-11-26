

# Build a machine learning model to predict salary  based on position for a given dataset
#https://drive.google.com/open?id=1jKfNxQkybZKprVpCkoL16mTjmSSnCol3

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import classification_report,confusion_matrix

#Read dataset

data=pd.read_csv("/home/shruti/Downloads/Position_Salaries.csv")
print(data.head())

X=data.iloc[:,1:2].values
print(X)

y=data.iloc[:,2].values
print(y)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.20)
print(X_train)
print(X_test)
print(y_train)
print(y_test)

regressor=DecisionTreeRegressor()
regressor.fit(X_train,y_train)

y_pred=regressor.predict(X_test)

print(confusion_matrix(y_test,y_pred))
print(classification_report(y_test,y_pred))

