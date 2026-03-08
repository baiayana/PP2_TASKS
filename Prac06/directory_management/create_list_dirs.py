# Create nested directories
# List files and folders
# Find files by extension

import os

nested_dir = "test_folder/subfolder/inner_folder"
os.makedirs(nested_dir, exist_ok=True)
print("Nested directories created.")

print("\nFiles and folders in current directory:")
for item in os.listdir("."):
    print(item)

print("\nPython files in current directory and subdirectories:")
for root, dirs, files in os.walk("."):
    for file in files:
        if file.endswith(".py"):
            print(os.path.join(root, file))