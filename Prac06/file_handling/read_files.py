# Read and print file contents

filename = "sample.txt"

try:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.read()
    print("File content:")
    print(content)
except FileNotFoundError:
    print("File does not exist.")