# Non-linear curve fitting

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Fitting function
def f(x,a,b):
    return a*np.exp(b*x)
# Experimental x and y data points

xData=np.array([1,2,3,4,5])
yData=np.array([1,9,50,300,1500])

#Plot experimental data points
plt.plot(xData,yData,'bo',label='Experimental-Data')

# INtial guess for the parameters
#IntialGuess=[1.0,1.0]

# Perform the curve_fit
popt,pcov=curve_fit(f,xData,yData)     # popt will give the optimized parameters for fitted curve and pcov will give the coverience matrix

print(popt)
print(pcov)
# x values for the fitted function
xFit=np.arange(0.0,5.0,0.01)

# Plot the Fitted function
plt.plot(xFit, f(xFit,*popt),'r',label='fit params: a=%5.3f, b=%5.3f' % tuple(popt))
plt.title('Non-Linear curve fitting')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()
plt.show()

 





































