#  import modules needed
import pandas as pd
from lifelines import CoxPHFitter

# Create a sample dataset
data = pd.DataFrame({
    'age': [45, 50, 55, 60, 65],
    'time_to_event': [10, 15, 20, 25, 30],
    'event_occurred': [1, 1, 0, 1, 0]  # 1 if event occurred, 0 otherwise
})

# Fit the Cox proportional hazards model
cph = CoxPHFitter()
cph.fit(data, duration_col='time_to_event', event_col='event_occurred')

# Print the summary
cph.print_summary()

# Get hazard ratios for each variable
hazard_ratios = cph.hazard_ratios_
print("Hazard Ratios:")
print(hazard_ratios)

# Predict survival probabilities for new data
new_data = pd.DataFrame({
    'age': [58],
})
survival_probs = cph.predict_survival_function(new_data)
print("Predicted survival probabilities:")
print(survival_probs)

# Calculate cumulative hazard rates
cumulative_hazard = cph.predict_cumulative_hazard(new_data)
print("Cumulative hazard rates:")
print(cumulative_hazard)

