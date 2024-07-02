# Predicting house prices based on size
# Step 1: Import necessary libraries
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt

# Step 2: Generate example dataset
# Create a dataset with house sizes (in square feet) and their corresponding prices (in $1000)
np.random.seed(0)
size = 2.5 * np.random.randn(100) + 25
price = 400 + 50 * size + np.random.randn(100) * 10

# Convert to a pandas DataFrame
data = pd.DataFrame({
    'Size': size,
    'Price': price
})

# print(data[0:5])

# Step 3: Exploratory Data Analysis
# Plot the data
plt.scatter(data['Size'], data['Price'])
plt.xlabel('Size (square feet)')
plt.ylabel('Price ($1000)')
plt.title('House Prices vs Size')
plt.show()

# Step 4: Prepare the data for training
# Defining the features (X) and target variable (y)
X = data[['Size']]
y = data['Price']

# Splitting the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# Step 5: Train the linear regression model
# Initializing and training the model
model = LinearRegression()
model.fit(X_train, y_train)

# Step 6: Make predictions and evaluate the model
# Making predictions on the testing set
y_pred = model.predict(X_test)

# Calculating mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plotting the regression line
plt.scatter(X_test, y_test, color='blue', label='Actual')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Predicted')
plt.xlabel('Size (square feet)')
plt.ylabel('Price ($1000)')
plt.title('Linear Regression: House Prices vs Size')
plt.legend()
plt.show()
