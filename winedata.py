import  pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics as m

data=pd.read_csv(r"C:\Users\madhura.anand\Desktop\pybasic\winedata.csv")
X=data.values.reshape(-1,12)
Y=data['quality'].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)
Y_pred=regressor.predict(X)
print(m.r2_score(Y,Y_pred))