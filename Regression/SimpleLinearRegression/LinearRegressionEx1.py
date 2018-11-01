
#Build a predictive linear regression model for given dataset, train the model for training set and test it against test dataset, plot the model using any plotting library.
#Dataset url - https://drive.google.com/open?id=17Z5YVgk4hSzPvguWkck6tRb6Z2JEWdgh

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/train.csv")
#print(df.head())
#print(df.shape)
#print(df.info())
#print(df.describe())
#print(df.columns)

#sns.pairplot(df)
#sns.distplot(df['x'])
#plt.show()

X=df['x']
print(X)
Y=df['y']
print(Y)

x_mean=np.mean(X)
print(x_mean)
y_mean=np.mean(Y)
print(y_mean)

m=len(X)
print(m)


