#https://machinelearningmastery.com/implement-simple-linear-regression-scratch-python/

import statistics
import re
import pandas as pd
import numpy as np
dataset=pd.read_excel(r"C:\Users\madhura.anand\Desktop\pybasic\pandasplay\swedata.xlsx", engine='xlrd')
x = dataset['X']
y = dataset['Y']
x_mean = statistics.mean(x)
y_mean = statistics.mean(y)
print(x_mean,y_mean)
X = np.stack((x, y), axis=0)
b1 = np.cov(X)/statistics.variance(x, x_mean)
b0 = y_mean - b1 * x_mean
print(b0)
print(b1)