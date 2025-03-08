import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y = [10, 20, 25, 30, 50]

# Create plot
plt.plot(x, y, marker='o', linestyle='-', color='b', label="Growth")

# Labels and title
plt.xlabel("X Axis (Time)")
plt.ylabel("Y Axis (Value)")
plt.title("Simple Line Chart")
plt.legend()

# Show plot
plt.show()
