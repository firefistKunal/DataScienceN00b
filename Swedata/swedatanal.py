import  numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_excel("swedata.xlsx")
SE=0
#print(data)
X=data['X']
#print(X)
Y=data['Y']
#print(Y)
learning_rate=0.00001
m,b=0,0
N=len(X)

def update_weights(m, b, X, Y, learning_rate):
    m_deriv = 0
    b_deriv = 0

    for i in range(len(X)):
        #  -2x(y - (mx + b))
        m_deriv += -2*X[i] * (Y[i] - (m*X[i] + b))
        # -2(y - (mx + b))
        b_deriv += -2*(Y[i] - (m*X[i] + b))

    # We subtract because the derivatives point in direction of steepest ascent
    m -= (m_deriv / float(N)) * learning_rate
    b -= (b_deriv / float(N)) * learning_rate

    return m, b
m1,b1=update_weights(m, b, X, Y, learning_rate)
#print(m1,b1)

Y_pred = m1*X + b # Equation of the line we modeled
#print(type(Y_pred))
for i in range(len(Y)):
    SE+=((Y_pred[i]-Y[i])**2)
    #print(SE)
    SE=SE/N
    #print(SE)
    MSE=np.sqrt(SE/N)
print("MEAN SQUARE ERROR IS ",MSE)



