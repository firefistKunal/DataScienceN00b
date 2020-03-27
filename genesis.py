import numpy as np 
import matplotlib.pyplot as plt 


x=np.arange(-6, 6, 0.1)

#x=float(input(" ddfg"))
y=1/(1+(np.e**-x))


fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2, 2)

ax1.scatter(x[:50],y[:50])
ax1.set_title("Exponential growth curve")
ax2.scatter(x[:50],np.log(y[:50]))
ax2.set_title("Log of expnential growth curve")
ax3.scatter(x,y)
ax3.set_title("Logistic curve")
ax4.scatter(x, np.log(y))
ax4.set_title("Log of Logistic curve")
fig.tight_layout(pad=2.0)
plt.show()