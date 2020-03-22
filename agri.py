#https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/

# import statistics
# import re
# import pandas as pd
# import numpy as np
# dataset=pd.read_excel("swedata.xlsx")
# x = dataset['X']
# y = dataset['Y']
# x_mean = statistics.mean(x)
# y_mean = statistics.mean(y)
# print(x_mean,y_mean)
# X = np.stack((x, y), axis=0)
# b1 = np.cov(X)/statistics.variance(x, x_mean)
# b0 = y_mean - b1 * x_mean
# print(b0)
# print(b1)


#This is the simpplest implementation for the linear regression using gradient algorithm.


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data=pd.read_excel("swedata.xlsx")
print(data)

# i am not splitting the data into training and testing etc, simply using it all to fit the curve
# also i'm not pre-processing the data assuming its already processed.
fig, (ax1, ax2) = plt.subplots(2)

ax1.scatter(data['X'], data['Y'])
ax1.set_title('X v Y distribution')
ax1.set(xlabel='X', ylabel='Y')

X, Y=data['X'], data['Y']

# Building the model
m=c=0 #m is slope and c is the y intercept of the line
L=0.0001 #the learning rate
epochs = 1000  # The number of iterations to perform gradient descent
n=len(data) #number of elements in training dataset

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X * (Y - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c

print(m, c)

#plotting the line against the data according to the model


Y_pred = m*X + c # Equation of the line we modeled

ax2.scatter(data['X'], data['Y'])
ax2.set_title('Line Obtained After Training')
ax2.set(xlabel='X', ylabel='Y')

prediction_space= ([min(X), max(X)])

ax2.plot(prediction_space, [min(Y_pred), max(Y_pred)], color='red')

plt.show()