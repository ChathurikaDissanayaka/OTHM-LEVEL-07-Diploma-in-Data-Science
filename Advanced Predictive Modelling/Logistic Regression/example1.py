# binary logistic regression

# import numpy module
import numpy

# import the method needed from sklearn module
from sklearn import linear_model

# x represents the size of a tumor in centimeters
# Note: x has to be reshaped into a column from a row for the LogisticRegression()
# function to work
x = numpy.array([3.78, 2.44, 2.09, 0.14, 1.72, 1.65, 4.92, 4.37, 4.96, 4.52, 3.69, 5.88]).reshape(-1,1)

# y represents whether or not the tumor is cancerous (0 for "No" 1 for "Yes")
y = numpy.array([0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1])

#  use LogisticRegression method to create a logistic regression object
# this method has a method called fit() that takes the independent and dependent 
# values as parameters and fills the regression object with data that describes
# the relationship
logr = linear_model.LogisticRegression()
logr.fit(x, y) 

# predict the tumor is cancerous where the size is 3.6cm
predicted = logr.predict(numpy.array([3.46]).reshape(-1,1))
print(predicted)

# ----------------------------------------------------------------------------------
# return value of log odds
# log_odds = logr.coef_
# odds = numpy.exp(log_odds)
# print(odds)

# this tells us that as the size of a tumor increases by 1mm the odds of it being a
# cancerous tumor increases by 4x
# ----------------------------------------------------------------------------------

# the coefficient and intercept vlaues can be used to find the probability
# that each tunor is cancerous
# create a function that uses the model's coefficient and intercept values
# to return a new value that represents probability that the given observation 
# is a tumor
def logit2prob(logr, x):
    log_odds = logr.coef_ * x + logr.intercept_
    odds = numpy.exp(log_odds)
    probability = odds /(1 + odds)
    return probability

print(logit2prob(logr, x))
