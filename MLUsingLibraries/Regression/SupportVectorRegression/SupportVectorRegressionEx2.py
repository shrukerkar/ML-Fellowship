
# For a given dataset predict number of bikes getting shared based on different parameters
#https://drive.google.com/open?id=1ohN2o3zSZ2Xuy4CIdTWN-dTmciUXizst

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.svm import SVR
from sklearn.preprocessing import StandardScaler


#Read Dataset

data=pd.read_csv("/home/shruti/Downloads/bike_sharing.csv",parse_dates=True,index_col='instant')
print(data.head())
print(data.shape)

data.rename(columns={'cnt':'total'},inplace=True)

#Visualizing dataset

data.plot(kind='scatter',x='temp',y='total',alpha=0.2)
plt.show()

sns.lmplot(x='temp',y='total',data=data,aspect=1.5,scatter_kws={'alpha':0.2})
plt.show()

#Dependent(y) and independent(X) variables

feature_col=['temp']
X=np.array(data[feature_col])
X.reshape(-1,1)
print(X.shape)
y=data.total
print(y.shape)


#FeatureScaling

sc_X=StandardScaler()
print(sc_X)
X=sc_X.fit_transform(X)
print(X)
sc_y=StandardScaler()
y=sc_y.fit_transform(y)
print(y)


regressor=SVR(kernel='rbf')
regressor.fit(X,y)

y_pred=regressor.predict(sc_X.transform(np.array([[6.5]])))

plt.scatter(X,y,color='red')
plt.plot(X,regressor.predict(X),color='blue')
plt.title('SVR')
plt.xlabel('Position Level')
plt.ylabel('salary')
plt.show()
