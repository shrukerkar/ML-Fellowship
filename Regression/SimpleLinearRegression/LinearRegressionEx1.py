
#Build a predictive linear regression model for given dataset, train the model for training set and test it against test dataset, plot the model using any plotting library.
#Dataset url - https://drive.google.com/open?id=17Z5YVgk4hSzPvguWkck6tRb6Z2JEWdgh

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Read data set
df_train=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/train.csv")
df_test=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/test.csv")


# Prints first 5 records
print(df_train.head())
print(df_test.head())
# prints shape of data
print(df_train.shape)
print(df_test.shape)
# Dataset information
print(df_train.info())
print(df_test.info())

# Describe dataset
print(df_train.describe())
print(df_test.describe())
#Print columns
print(df_train.columns)
print(df_test.columns)

#sns.pairplot(df)
#sns.distplot(df['x'])
#plt.show()


#Collecting X and Y
X=df_train['x']
print(X)
Y=df_train['y']
print(Y)

# mean X and Y
x_mean=np.mean(X)
print(x_mean)
y_mean=np.mean(Y)
print(y_mean)

#Total number of values

m=len(X)
print(m)

numerator=0
denominator=0

for i in range (m):
    numerator=(X[i]-x_mean)*(Y[i]-y_mean)
    denominator=(X[i]-x_mean)**2

b1=numerator/denominator
b0=y_mean-(b1*x_mean)
print(b1,b0)


x_max=np.max(X)
x_min=np.min(X)

x=np.linspace(x_min,x_max,1000)
y=b0+b1*x

plt.plot(x,y,color='r',label='regression line')
plt.plot(X,Y,c='g',label='scatter plot')
plt.legend()
plt.show()

rmse=0
for i in range(m):
    y_pred=b0+b1*X[i]