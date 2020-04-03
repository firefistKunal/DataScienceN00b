import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

data=pd.read_excel("swedata.xlsx") #Importing the data

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2) #initializing the graph

####################### Using math formula for the linear regression using gradient algorithm ##########################

#splitting the data randomly into train and test 80%-20%
msk = np.random.rand(len(data)) < 0.8
train, test= data[msk], data[~msk]



# plotting the train data in the graph to visualize
ax1.scatter(train['X'], train['Y'])
ax1.set_title('#1')
ax1.set(xlabel='X-Train', ylabel='Y-Train')

# Building the model
X_train, Y_train, X_test, Y_test =train['X'], train['Y'], test['X'], test['Y']

m=c=0 #m is slope and c is the y intercept of the line
L=0.0001 #the learning rate
epochs = 1000  # The number of iterations to perform gradient descent
n=len(data) #number of elements in training dataset

# Performing Gradient Descent 
for i in range(epochs): 
    Y_pred = m*X_train + c  # The current predicted value of Y
    D_m = (-2/n) * sum(X_train * (Y_train - Y_pred))  # Derivative wrt m
    D_c = (-2/n) * sum(Y_train - Y_pred)  # Derivative wrt c
    m = m - L * D_m  # Update m
    c = c - L * D_c  # Update c

print(m, c)

Y_pred = m*X_test + c #Predictiong the Y for test data using the equation of the line we modeled

#plotting the graph for test data

ax2.scatter(test['X'], test['Y'])
ax2.set_title('#2')
ax2.set(xlabel='X-Test', ylabel='Y-Test')
ax2.plot([min(X_test), max(X_test)], [min(Y_pred), max(Y_pred)], color='red')



###########################    Same thing with the sklearn modules    #####################################
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Separating the data into independent and dependent variables and 
# Converting each dataframe into a numpy array since each dataframe contains only one column 
X, Y=np.array(data['X']).reshape(-1, 1), np.array(data['Y']).reshape(-1, 1)

# Splitting the data into training and testing data
Xtrain, Xtest, Ytrain, Ytest = train_test_split(X, Y, test_size = 0.20) 
#please note that here we didn't use "underscore" in variable to distinguish from variables used in previous method

#plotting the train data to visualize
ax3.scatter(Xtrain, Ytrain)
ax3.set_title('#3')
ax3.set(xlabel='X-Train', ylabel='Y-Train')

#Building the model
reg=LinearRegression()
reg.fit(Xtrain, Ytrain)

print(reg.score(Xtest, Ytest)) # Best possible score is 1.0. It can also be negative if you give stupid arbitrary data

y_pred=reg.predict(Xtest)# Predicting Y for the test data

#plotting the graph for test data
ax4.scatter(Xtest, Ytest, color='blue')
ax4.plot(Xtest, y_pred, color='red')
ax4.set_title('#4')
ax4.set(xlabel='X-Test', ylabel='Y-Test')

fig.tight_layout(pad=2.0)
plt.show()