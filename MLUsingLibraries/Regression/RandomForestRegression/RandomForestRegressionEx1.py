
# Build a machine learning model to predict salary  based on position for a given dataset
#https://drive.google.com/open?id=1jKfNxQkybZKprVpCkoL16mTjmSSnCol3


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

#Read dataset
data=pd.read_csv("/home/shruti/Downloads/Position_Salaries.csv")
print(data.head())


#Select dependent and independent variable

X=data.iloc[:,1:2].values
y=data.iloc[:,2].values

print(X)
print(y)
#Training and making predictions

regressor=RandomForestRegressor(n_estimators=10,random_state=0)
regressor.fit(X,y)

#prediction
y_pred=regressor.predict([[6.5]])
print(y_pred)

X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title("Truth or Bluff")
plt.xlabel("position level")
plt.ylabel("Salary")
plt.show()