
#Build a machine learning model to predict user will click the ad or not based on his experience and estimated salary for a given dataset.
#https://drive.google.com/open?id=1I8KsCufEa47XvzrkxhntEWSy1Su0E0NY


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


data=pd.read_csv("/home/shruti/Downloads/Social_Network_Ads.csv")
print(data.head())

sns.countplot(x=data[''])
