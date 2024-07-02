import numpy as np
from scipy.optimize import linprog
import matplotlib.pyplot as plt

# Objective function coefficients (cost per unit)
c = [2, 3, 1]

# Inequality constraint matrix (nutritional requirements)
A = [
    [-200, -300, -100],  # Calories (>= 500)
    [-20, -30, -1],      # Protein (>= 6)
    [-10, -20, 0]        # Fat (>= 10)
]

# Inequality constraint vector
b = [-500, -6, -10]

# Bounds for each food (non-negative quantities)
x_bounds = (0, None)
bounds = [x_bounds, x_bounds, x_bounds]

# Solve linear programming problem
result = linprog(c, A_ub=A, b_ub=b, bounds=bounds, method='highs')

# Extract optimal solution
optimal_quantities = result.x
minimized_cost = result.fun

# Display results
print('Optimal cost:', minimized_cost)
print('Chicken:', optimal_quantities[0], 'units')
print('Beef:', optimal_quantities[1], 'units')
print('Rice:', optimal_quantities[2], 'units')

# Visualization
foods = ['Chicken', 'Beef', 'Rice']
plt.figure(figsize=(10, 5))

# Bar plot for optimal quantities
plt.subplot(1, 2, 1)
plt.bar(foods, optimal_quantities, color=['blue', 'green', 'orange'])
plt.title('Optimal Quantities of Foods')
plt.xlabel('Food')
plt.ylabel('Quantity')

# Cost analysis
plt.subplot(1, 2, 2)
plt.bar(['Cost'], minimized_cost, color='red')
plt.title('Minimized Cost')
plt.ylabel('Cost')
plt.ylim(0, 30)  # Adjust ylim for better visualization if necessary

plt.tight_layout()
plt.show()
