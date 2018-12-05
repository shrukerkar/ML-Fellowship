
#For a given dataset predict number of bikes getting shared based on different parameters
#https://drive.google.com/open?id=1ohN2o3zSZ2Xuy4CIdTWN-dTmciUXizst

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
import seaborn as sns
#Read dataset

data=pd.read_csv("/home/shruti/Downloads/bike_sharing.csv")

#print(data)

print(data.head())
print(data.info)


data.rename(columns={'cnt':'total'},inplace=True)

#Visualizing dataset

data.plot(kind='scatter',x='temp',y='total',alpha=0.2)
plt.show()

sns.lmplot(x='temp',y='total',data=data,aspect=1.5,scatter_kws={'alpha':0.2})
plt.show()

#Dependent(y) and independent(X) variables

feature_col=['temp']
X=np.array(data[feature_col])
#X.reshape(-1,1)
print(X.shape)
y=data.total
print(y.shape)

#Training and making predictions

regressor=RandomForestRegressor()
regressor.fit(X,y)

y_pred=regressor.predict([[56]])

print(y_pred)


X_grid=np.arange(min(X),max(X),0.01)
X_grid=X_grid.reshape((len(X_grid),1))
plt.scatter(X,y,color='red')
plt.plot(X_grid,regressor.predict(X_grid),color='blue')
plt.title("Bike sharing")
plt.xlabel("Temprature")
plt.ylabel("Count")
plt.show()
