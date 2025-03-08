import pandas as pd

# Creating a DataFrame
data = {
    "Product": ["Laptop", "Phone", "Tablet"],
    "Price": [800, 500, 300]
}

df = pd.DataFrame(data)

# Save DataFrame to CSV
df.to_csv("products.csv", index=False)

print("CSV file saved successfully!")
