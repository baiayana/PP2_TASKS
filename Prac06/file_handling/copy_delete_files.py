# Copy and back up files using shutil
# Delete files safely

import shutil
import os

source_file = "sample.txt"
backup_file = "sample_backup.txt"

if os.path.exists(source_file):
    shutil.copy(source_file, backup_file)
    print("Backup created:", backup_file)
else:
    print("Source file not found.")

file_to_delete = "sample_backup.txt"

if os.path.exists(file_to_delete):
    os.remove(file_to_delete)
    print("File deleted safely:", file_to_delete)
else:
    print("File not found, nothing to delete.")