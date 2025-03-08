import seaborn as sns
import matplotlib.pyplot as plt

# Sample Data
categories = ["AI", "ML", "Data Science", "Cybersecurity", "Robotics"]
values = [80, 75, 90, 60, 70]

# Create a Seaborn bar chart
sns.barplot(x=categories, y=values, palette="coolwarm")

# Labels and title
plt.xlabel("Categories")
plt.ylabel("Popularity Score")
plt.title("Popularity of AI Fields")

# Show plot
plt.show()
