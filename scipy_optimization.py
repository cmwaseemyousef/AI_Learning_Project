from scipy.optimize import minimize

# Function to Minimize (Example: x^2 + 5x + 6)
def objective_function(x):
    return x**2 + 5*x + 6

# Finding the Minimum Value
result = minimize(objective_function, x0=0)

print("Optimal Value:", result.x[0])
print("Function Value at Optimum:", result.fun)
