
#The data given in the url  is related with direct marketing campaigns of a banking institution.
# The marketing campaigns were based on phone calls.
# Often, more than one contact to the same client was required, in order to access if the product
# (bank term deposit) would be ('yes') or not ('no') subscribed. Build a model to predict whether client will subscribe to term deposit
#https://drive.google.com/open?id=1E0EURgsF3L9Bt5hnOalE0d4Tw9mIOgTn

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#Read dataset
data=pd.read_csv("/home/shruti/Downloads/bank.csv",sep=";")
print(data.head())
print(data.shape)

#Number of columns
print(data.columns.values)

#Sum Of null values
print(data.isnull().sum())

#Visualization
sns.countplot(y="job",data=data)
plt.show()

sns.countplot(x="marital",data=data)
plt.show()

sns.countplot(x="default",data=data)
plt.show()

sns.countplot(x="housing",data=data)
plt.show()

sns.countplot(x="poutcome",data=data)
plt.show()

sns.countplot(x="y",data=data)
plt.show()

sns.countplot(x="age",data=data)
plt.show()























