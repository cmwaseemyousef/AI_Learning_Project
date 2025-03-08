# Creating a dictionary
student = {
    "name": "Waseem",
    "age": 25,
    "course": "AI Engineering"
}

# Accessing values
print("Name:", student["name"])
print("Age:", student["age"])

# Adding a new key-value pair
student["grade"] = "A"
print("Updated Dictionary:", student)

# Looping through dictionary
for key, value in student.items():
    print(key, ":", value)
