# Random Forest for Predicting Stock Prices
# Step 1: Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Step 2: Load and Prepare Data
# Generate synthetic data
np.random.seed(42)
dates = pd.date_range('2020-01-01', periods=200)
prices = np.cumsum(np.random.randn(200)) + 100
df = pd.DataFrame({'Date': dates, 'Price': prices})
# print(df[0:5])

# Feature engineering
df['Day'] = df['Date'].dt.dayofyear
df['Year'] = df['Date'].dt.year

# Step 3: Split the data
X = df[['Day', 'Year']]
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 4: Train the Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Step 5: Make Predictions
y_pred = model.predict(X_test)

# Calculate metrics
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f'Mean Squared Error: {mse}')
print(f'R^2 Score: {r2}')

# Step 6: Plot the Results
plt.scatter(y_test, y_pred)
plt.xlabel('Actual Prices')
plt.ylabel('Predicted Prices')
plt.title('Actual vs Predicted Stock Prices')
plt.show()
