
# For a given dataset predict number of bikes getting shared based on different parameters
#https://drive.google.com/open?id=1ohN2o3zSZ2Xuy4CIdTWN-dTmciUXizst

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("/home/shruti/Downloads/bike_sharing.csv",parse_dates=True)
print(data.head())
print(data.shape)

