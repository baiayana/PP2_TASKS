# Create a text file and write sample data
# Append new lines and verify content

filename = "sample.txt"

with open(filename, "w", encoding="utf-8") as file:
    file.write("Hello, this is the first line.\n")
    file.write("This is the second line.\n")

print("Initial file created.")

with open(filename, "a", encoding="utf-8") as file:
    file.write("This line was appended.\n")
    file.write("Another appended line.\n")

print("New lines appended.")

with open(filename, "r", encoding="utf-8") as file:
    content = file.read()

print("\nFile content:")
print(content)