# Open a file in append mode ('a')
file = open("data.txt", "a")

# Add new lines to the file
file.write("Python is great for AI development.\n")
file.write("Let's build some cool AI projects!\n")

# Close the file
file.close()

print("New data appended successfully!")
