
#Build a predictive linear regression model for given dataset, given temperature,
# humidity, wind speed , wind bearing,
# visibility, pressure  predict apparent temperature
#https://drive.google.com/open?id=1WsJxbsh51SL1UhT0xEvNynZTKy4nOwLM


#%matplotlib inline
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (20.0, 10.0)
from mpl_toolkits.mplot3d import Axes3D


data = pd.read_csv('/home/shruti/Downloads/weatherHistory.csv',parse_dates=True)
print(data.shape)
print(data.head())


humidity=data['Humidity'].values
windspeed=data['Wind Speed (km/h)'].values
windbearing=data['Wind Bearing (degrees)'].values
visiblity= data['Visibility (km)'].values
pressure=data['Pressure (millibars)'].values
temprature=data['Temperature (C)'].values
# Ploting scatter plot
fig = plt.figure()
ax = Axes3D(fig)
ax.scatter(humidity,windspeed,windbearing,visiblity,pressure,color='#ef1234')
plt.show()


m = len(humidity)
x0 = np.ones(m)
X = np.array([x0,humidity,windspeed]).T
# Initial Coefficients
B = np.array([0, 0, 0])
Y = np.array(temprature)
alpha = 0.0001

def cost_function(X, Y, B):
    m = len(Y)
    J = np.sum((X.dot(B) - Y) ** 2)/(2 * m)
    return J

inital_cost = cost_function(X, Y, B)
print(inital_cost)


def gradient_descent(X, Y, B, alpha, iterations):
    cost_history = [0] * iterations
    m = len(Y)

    for iteration in range(iterations):
        # Hypothesis Values
        h = X.dot(B)
        # Difference b/w Hypothesis and Actual Y
        loss = h - Y
        # Gradient Calculation
        gradient = X.T.dot(loss) / m
        # Changing Values of B using Gradient
        B = B - alpha * gradient
        # New Cost Value
        cost = cost_function(X, Y, B)
        cost_history[iteration] = cost

    return B, cost_history

# 100000 Iterations
newB, cost_history = gradient_descent(X, Y, B, alpha, 100000)

# New Values of B
print(newB)

# Final Cost of new B
print(cost_history[-1])


#  RMSE
def rmse(Y, Y_pred):
    rmse = np.sqrt(sum((Y - Y_pred) ** 2) / len(Y))
    return rmse

# R2 Score
def r2_score(Y, Y_pred):
    mean_y = np.mean(Y)
    ss_tot = sum((Y - mean_y) ** 2)
    ss_res = sum((Y - Y_pred) ** 2)
    r2 = 1 - (ss_res / ss_tot)
    return r2

Y_pred = X.dot(newB)

print(rmse(Y, Y_pred))
print(r2_score(Y, Y_pred))

