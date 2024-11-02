import os

# Get the current working directory
current_directory = os.getcwd()

# Construct the full path to the URDF file
file_name = "r068.urdf"
file_path = os.path.join(current_directory, file_name)

# Access the file using the full path
with open(file_path, 'r') as file:
    content = file.read()
    print(content)