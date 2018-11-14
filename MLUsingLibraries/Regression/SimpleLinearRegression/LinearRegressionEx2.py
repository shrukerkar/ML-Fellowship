
#  For a given dataset predict number of bikes getting shared based on temperature of the day
# https://drive.google.com/open?id=1ohN2o3zSZ2Xuy4CIdTWN-dTmciUXizst

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns



data=pd.read_csv("/home/shruti/Downloads/bike_sharing.csv")
print(data.head())
print(data.shape)
print(data.corr)


sns.regplot(x=data["temp"],y=["cnt"])
plt.show()

