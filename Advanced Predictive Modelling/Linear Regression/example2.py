# multiple linear regression

# import pandas library
import pandas
# import sklearn 
from sklearn import linear_model

# read csv file(data set) and return a data frame object that is pointed to the data set
df = pandas.read_csv("data.csv")

# get the required columns from the data frame object
# independant variable
x = df[['weight', 'volume']]
# dependant variable
y = df['co2']

# from the sklearn module we will use the LinearRegression() method 
# to create a linear regression object that has a method called fit() that takes
# the independant and dependant values as parameters and fills the regression
# object with data that describes the relationship
regr = linear_model.LinearRegression()
regr.fit(x, y)

# predict the co2 emission of a car where the weight is 2300kg, and the volume is 1300cm3
predictco2 = regr.predict([[2300, 1300]])

#  print the predicted value
print(predictco2)

#  print the coefficient values of the regression object
print(regr.coef_)

# increase the weight by 1000kg
predictco2_2 = regr.predict([[3300, 1300]])
print(predictco2_2)
