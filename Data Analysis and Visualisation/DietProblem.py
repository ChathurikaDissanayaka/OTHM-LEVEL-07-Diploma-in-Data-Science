# Import necessary libraries
import numpy as np
from scipy.optimize import linprog

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

# Display results
print('Optimal cost:', result.fun)
print('Chicken:', result.x[0], 'units')
print('Beef:', result.x[1], 'units')
print('Rice:', result.x[2], 'units')
