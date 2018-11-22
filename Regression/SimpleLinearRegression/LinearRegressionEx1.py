
#Build a predictive linear regression model for given dataset, train the model for training set and test it against test dataset, plot the model using any plotting library.
#Dataset url - https://drive.google.com/open?id=17Z5YVgk4hSzPvguWkck6tRb6Z2JEWdgh

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score

def estimate_coeffiecient(X_train,y_train):
    n=np.size(X_train)
    mean_X,mean_y=np.mean(X_train),np.mean(y_train)
    SS_xy=np.sum(y_train*X_train- n*mean_y*mean_X)
    SS_xx=np.sum(X_train*X_train- n*mean_X*mean_X)

    b1=SS_xy/SS_xx
    b0=mean_y - b1*mean_X

    return(b0,b1)

def regression_line(X_test,y_test,b):
    plt.scatter(X_test,y_test,color="m",marker="o",s=30)
    y_pred=b[0]+b[1]*X_test
    plt.plot(X_test,y_pred,color="g")

    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.show()


#Read data set
def main():
    df_train=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/train.csv")
    df_test=pd.read_csv("/home/shruti/Downloads/simple-linear-regression/test.csv")

# Train test split
    X_train=np.array(df_train['x'])
    y_train=np.array(df_train['y'])
    X_test=np.array(df_test['x'])
    y_test=np.array(df_test['y'])

    print(X_train)
    print(y_test)
    print(X_test)
    print(y_test)

    b=estimate_coeffiecient(X_train,y_train)
    print("Estimated coefficient:\n b0={} \n b1={}".format(b[0],b[1]))
    regression_line(X_test,y_test,b)


if __name__=="__main__":
    main()
#x_train=x_train.reshape(-1,1)
#print(x_train)
#x_test=x_test.reshape(-1,1)
#print(x_test)

# total number of training examples and learning rate

#n=len(x_train)
#alpha=0.0001

# defining b0 and b1
#b0=np.zeros((n,1))
#b1=np.zeros((n,1))

# Calculating R2 Score

#print(r2_score(y_test,y_pred))

#rmse = 0
#for i in range(n):
#    y_pred = b0 + b1 * x_test
#    rmse += (y_test - y_pred) ** 2
#rmse = np.sqrt(rmse/n)
#print(rmse)

#ss_r=0
#ss_t=0

#mean_y=np.mean(y_test)
#for i in range(n):
#    y_pred=b0+b1*x_test
#    ss_t+=(y_test-mean_y)**2
#    ss_r+=(y_test-y_pred)**2
#r2_score=1-(ss_r/ss_t)
#print(r2_score)


#iter=0

#while(iter<1000):
#    y=b0+b1*x_train
#    error=y-y_train
#    mean_sqaure_error=np.sum(error**2)
#    mean_sqaure_error=mean_sqaure_error/n
#    b0=b0-alpha*2*np.sum(error)/n
#    b1=b1-alpha*2*np.sum(error*x_train)/n
#    iter+=1
#    if(iter%10==0):
#        print(mean_sqaure_error)




#y_pred=b0+b1*x_test
#print()

# ploting x_test and y_test
#y_plot=[]
#for i in range(100):
#      y_plot.append(b0+b1*i)
#plt.figure(figsize=(10,10))
#plt.scatter(x_train,y_train,color='red',label="GT")
#plt.plot(range(len(y_plot)),y_plot,color='black',label='pred')
#plt.legend()
#plt.show()





