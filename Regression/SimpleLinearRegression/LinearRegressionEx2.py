
#Build a predictive linear regression model for given dataset, given humidity predict apparent temperature
#https://drive.google.com/open?id=1WsJxbsh51SL1UhT0xEvNynZTKy4nOwLM

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split

df=pd.read_csv("/home/shruti/Downloads/weatherHistory.csv")
print(df.head())

print(df.describe(include=['O']))

print(df.corr())

data_set=df.iloc[:,[0,3,4,5,8]]
print(data_set.corr())

sns.regplot(x=data_set["Temperature (C)"],y=data_set["Humidity"])
plt.show()
#ns.regplot(x=data_set["Temperature (C)"], y=data_set["Apparent Temperature (C)"])
#lt.show()

#Remove Outliers in dataset

outliers=[]
def dect_outlier(data):
    limit=3
    mean=np.mean(data)
    std=np.std(data)
    for i in data:
        z_score=(i-mean)/std
        if np.abs(z_score)>limit:
            outliers.append(i)
    return outliers
outlier_data=dect_outlier(data_set["Humidity"])
print(outlier_data)

final_data_set=data_set[data_set["Humidity"]>0.15]
print(final_data_set)

#sns.regplot(x=final_data_set["Temperature (C)"],y=final_data_set["Humidity"])
#plt.show()


#final_data_set=data_set[data_set["Humidity"]<=0.15]
#print(final_data_set)

y=final_data_set.iloc[:,[3]]
print(y)
X=final_data_set.iloc[:,[2]]
print(X)

X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)
print(X_train.shape)
print(y_train.shape)

alpha=0.0001
iterations=1000

m=len(X_train)
print(m)
def gradient_descent():
    y_pred=np.array(0)
    w=b=i=0
    db=0
    dw=0
    while i < iterations:
        for j in range(m):
            db +=((b+w*X_train[j])-y_train[j])
            dw +=((b+w*X_train[j])-y_train[j])*X_train[j]
        b= b-((alpha*db)/m)
        w= w-((alpha*dw)/m)
        i+=1
    for i in range(len(X_test)):
        y_pred=(b+w*X_test)
        y_pred=float(str(y_pred)[0:3])
    print("Accuracy",avgerror(np.asarray(y_pred)),type(y_pred))

def avgerror(y_pred_test):
    total_error=0
    for i in range(0,len(y_test)):
        total_error+=abs((y_pred_test[i] - y_test[i])/y_test[i])
    total_error=total_error/len(y_test)
    accuracy=1- total_error
    return accuracy * 100


def graph(y_pred):
    plt.scatter(X_test, y_test, color='g', label='whole data')
    plt.plot(X_test, y_pred, color='r', label='predicted value')
    plt.legend()
    plt.show()

if __name__=='__main__':

    gradient_descent()