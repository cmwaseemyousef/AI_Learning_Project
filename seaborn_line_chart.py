import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
data = {"Day": [1, 2, 3, 4, 5],
        "Sales": [100, 250, 400, 300, 500]}

# Create a line plot
sns.lineplot(x=data["Day"], y=data["Sales"], marker="o", color="b")

# Labels and title
plt.xlabel("Day")
plt.ylabel("Sales ($)")
plt.title("Daily Sales Trend")

# Show plot
plt.show()
