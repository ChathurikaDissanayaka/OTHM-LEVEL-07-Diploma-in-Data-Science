# import the modules need
import matplotlib.pyplot as plt
from scipy import stats

# x values
x = [5,7,8,7,2,17,2,9,4,11,12,9,6]

#  y values 
y = [99,86,87,88,111,86,103,87,94,78,77,85,86]

# execute a method that returns some important key values of liinear regression
slope, intercept, r, p, std_err = stats.linregress(x,y)

# function that uses the slope and intercept values to return a new value 
# this new value represents where on the y-axis the corresponding x value will be placed
def myfunc(x):
    return slope * x + intercept # mx + c

# run each value of the x array through the function.
# this will result in a new array with new values for the y-axis
myModel = list(map(myfunc, x))

# draw the original scatter plot 
plt.scatter(x, y)
# draw the line of linear regression
plt.plot(x, myModel)
# display the diagram
plt.show()
