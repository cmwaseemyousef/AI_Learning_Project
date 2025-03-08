import matplotlib.pyplot as plt

# Data
categories = ["AI", "ML", "Data Science", "Cybersecurity", "Robotics"]
values = [80, 75, 90, 60, 70]

# Create bar chart
plt.bar(categories, values, color=['red', 'blue', 'green', 'purple', 'orange'])

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Scores")
plt.title("Popularity of AI Fields")

# Show plot
plt.show()
