import pandas as pd  # Import Pandas

# Creating a DataFrame
data = {
    "Name": ["Waseem", "John", "Alice"],
    "Age": [25, 30, 22],
    "Course": ["AI", "ML", "Data Science"]
}

df = pd.DataFrame(data)  # Create DataFrame

print("DataFrame:\n", df)  # Display Data
