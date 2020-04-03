import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

SE=0

MSE=0
data=pd.read_excel("swedata.xlsx")
X=data['X'].values.reshape(-1,1)
Y=data['Y'].values.reshape(-1,1)
N=len(X)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
print(regressor.intercept_)
print(regressor.coef_)
Y_pred = regressor.coef_*X + regressor.intercept_
for i in range(N):
    SE+=((Y_pred[i]-Y[i])**2)
    #print(SE)
    SE=SE/N
    #print(SE)
    MSE=np.sqrt(SE/N)
print("MEAN SQUARE ERROR IS",MSE)