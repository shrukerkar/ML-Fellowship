
#Apply following steps to dataset given in a url
#https://drive.google.com/open?id=1NKMy-zIT3tfpNLnA7G0EmPxgZe0OPXp_
#Handling missing data
#Handling categorical data
#Split the dataset into training set and test set
#Feature scaling

import pandas as pd
import numpy as np




#Read Data
data_url="/home/shruti/Downloads/data_preprocessing.csv"

df=pd.read_csv(data_url)

print(df.shape)

#X=df.iloc[:,:-1].values
#y=df.iloc[:,3].values

#Handling Missing Data
#1.Find number of Nan in data

print(df.isnull().sum())  # Total number of Nan in data

print(df.info())

print(df.describe())

#2.Drop Missing Values

print(df.dropna())

print(df.info())

#3.Filling Missing Values
#For mean
mean_value_age=df['Age'].mean()
df['Age']=df['Age'].fillna(mean_value_age)
print(df['Age'])

mean_value_salary=df['Salary'].mean()
df['Salary']=df['Salary'].fillna(mean_value_salary)
print(df['Salary'])

#4.Handling categorial Data
#Encoding class labels
class_mapping={label:idx for idx,label in enumerate(np.unique(df['Country']))}
print(class_mapping)

df['Country']=df['Country'].map(class_mapping)
print(df)

#Onehotencoder
obj_df=df.select_dtypes(include=['object']).copy()
print(obj_df.head())
#print(obj_df.dtypes)

obj_df['Country']=obj_df['Country'].astype('category')
print(obj_df.dtypes)

print(pd.get_dummies(obj_df,columns=['Country']).head())



#5.Split data set into training and test set

train_data=df[0:8]

print(train_data)

test_data=df[8:]

print(test_data)

#from sklearn.model_selection import train_test_split

#X_train,X_test,y_train,y_test= train_test_split(X,y,test_size=0.20)

#print(X_train)
#print(X_test)

#6.Feature Scaling

