# Move/copy files between directories

import os
import shutil

source_dir = "source_files"
destination_dir = "destination_files"

os.makedirs(source_dir, exist_ok=True)
os.makedirs(destination_dir, exist_ok=True)

source_file = os.path.join(source_dir, "example.txt")

with open(source_file, "w", encoding="utf-8") as file:
    file.write("This file will be moved and copied.")

copied_file = os.path.join(destination_dir, "copied_example.txt")
shutil.copy(source_file, copied_file)
print("File copied to:", copied_file)

moved_file = os.path.join(destination_dir, "moved_example.txt")
shutil.move(source_file, moved_file)
print("File moved to:", moved_file)