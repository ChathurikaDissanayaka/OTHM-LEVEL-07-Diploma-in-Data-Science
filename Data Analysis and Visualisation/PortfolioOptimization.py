# Import necessary libraries
from scipy.optimize import minimize

# Objective function (risk)
def objective(x):
    return x[0]**2 + x[1]**2 + x[2]**2

# Equality constraint (total investment = $1000)
def constraint1(x):
    return x[0] + x[1] + x[2] - 1000

# Bounds for each asset (minimum investment requirements)
bnds = ((200, None), (150, None), (100, None))

# Initial guess
x0 = [200, 150, 100]

# Constraints dictionary
cons = {'type': 'eq', 'fun': constraint1}

# Solve nonlinear programming problem
result = minimize(objective, x0, method='SLSQP', bounds=bnds, constraints=cons)

# Display results
print('Minimum risk:', result.fun)
print('Investment in asset 1:', result.x[0])
print('Investment in asset 2:', result.x[1])
print('Investment in asset 3:', result.x[2])
