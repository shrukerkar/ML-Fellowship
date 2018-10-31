
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

print(df)

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
onehot_encoded=list()
for value in class_mapping:
    num=[0 for _ in range(len(df['Country']))]
    num[value]=1
    onehot_encoded.append(num)
print(onehot_encoded)

#5.Split data set into training and test set


