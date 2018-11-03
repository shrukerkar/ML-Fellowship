
#Build a predictive linear regression model for given dataset, train the model for training set and test it against test dataset, plot the model using any plotting library.
#Dataset url - https://drive.google.com/open?id=17Z5YVgk4hSzPvguWkck6tRb6Z2JEWdgh

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Read data set
df_train=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/train.csv")
df_test=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/test.csv")

# Train test split
x_train=np.array(df_train['x'])
y_train=np.array(df_train['y'])
x_test=np.array(df_test['x'])
y_test=np.array(df_test['y'])

print(x_train)
print(y_test)
print(x_test)
print(y_test)


x_train=x_train.reshape(-1,1)
print(x_train)
x_test=x_test.reshape(-1,1)
print(x_test)

# total number of training examples and learning rate

n=len(x_train)
alpha=0.0001

# defining b0 and b1
b0=np.zeros((n,1))
b1=np.zeros((n,1))

# Calculating R2 Score

rmse = 0
for i in range(n):
    y_pred = b0 + b1 * x_test
    rmse += (y_test - y_pred) ** 2
rmse = np.sqrt(rmse/n)
print(rmse)

ss_r=0
ss_t=0

mean_y=np.mean(y_test)
for i in range(n):
    y_pred=b0+b1*x_test
    ss_t+=(y_test-mean_y)**2
    ss_r+=(y_test-y_pred)**2
r2_score=1-(ss_r/ss_t)
print(r2_score)


iter=0

while(iter<1000):
    y=b0+b1*x_train
    error=y-y_train
    mean_sqaure_error=np.sum(error**2)
    mean_sqaure_error=mean_sqaure_error/n
    b0=b0-alpha*2*np.sum(error)/n
    b1=b1-alpha*2*np.sum(error*x_train)/n
    iter+=1
    if(iter%10==0):
        print(mean_sqaure_error)

# ploting x_test and y_test
y_plot=[]
for i in range(100):
      y_plot.append(b0+b1*i)
plt.figure(figsize=(10,10))
plt.scatter(x_train,y_train,color='red',label="GT")
plt.plot(range(len(y_plot)),y_plot,color='black',label='pred')
plt.legend()
plt.show()





