# Forecasting daily temperatures
# Step 1: Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from statsmodels.tsa.seasonal import STL
from statsmodels.tsa.arima.model import ARIMA

# Step 2: Generate example dataset
# Create a time series dataset
np.random.seed(0)
date_range = pd.date_range(start='1/1/2020', periods=365, freq='D')
temperatures = 20 + 10 * np.sin(2 * np.pi * date_range.dayofyear / 365) + np.random.randn(len(date_range))

# Convert to a pandas DataFrame
data = pd.DataFrame({
    'Date': date_range,
    'Temperature': temperatures
}).set_index('Date')

print(data[0:5])

# Step 3: Exploratory Data Analysis
# Plot the time series data
data.plot()
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('Daily Temperature Data')
plt.show()

# Step 4: Decompose the time series
# Decompose the time series using STL (Seasonal and Trend decomposition using Loess)
stl = STL(data['Temperature'], seasonal=13)
result = stl.fit()

# Plot the decomposed components
result.plot()
plt.show()

# Step 5: Prepare the data for ARIMA model
# Use the residual component (remainder) for ARIMA modeling
residual = result.resid

# Step 6: Train the ARIMA model
# Initialize and train the ARIMA model on the residual component
model = ARIMA(residual, order=(1, 0, 1))
fitted_model = model.fit()

# Step 7: Make predictions and plotting the results
# Making predictions on the residuals
forecast_steps = 30  # Predicting next 30 days
forecast_residuals = fitted_model.get_forecast(steps=forecast_steps).predicted_mean

# Extract the seasonal and trend components for the forecast period
seasonal_component = result.seasonal[-13:]  # Seasonal component for the last period
seasonal_forecast = np.tile(seasonal_component, int(np.ceil(forecast_steps / 13)))[:forecast_steps]

# Extend the trend component to cover the forecast period
trend_component = np.linspace(result.trend.iloc[-13:].mean(), result.trend.iloc[-13:].mean(), forecast_steps)

# Reconstruct the forecasted values
forecast_dates = pd.date_range(start=data.index[-1] + pd.Timedelta(days=1), periods=forecast_steps, freq='D')
forecast = trend_component + seasonal_forecast + forecast_residuals

# Create a DataFrame for the forecast
forecast_df = pd.DataFrame({
    'Date': forecast_dates,
    'Forecast': forecast
}).set_index('Date')

# Plot the actual and forecasted values
plt.plot(data, label='Actual Temperature')
plt.plot(forecast_df, label='Forecasted Temperature', linestyle='--')
plt.xlabel('Date')
plt.ylabel('Temperature (°C)')
plt.title('ARIMA Forecast: Daily Temperature Data')
plt.legend()
plt.show()
