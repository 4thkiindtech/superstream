import os

base_directory = "/path/to/your/base/directory"
new_directory = "subdirectory_name"

# Create a new directory
os.makedirs(os.path.join(base_directory, new_directory))