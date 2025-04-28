import os

# Get the absolute path of the current script
current_dir = os.path.dirname(os.path.abspath(__file__))
print(current_dir)
# Now, you can build the path to 'main.py' relative to the current directory
file_path = os.path.join(current_dir, 'test.py')
print(file_path)
print(file_path)
