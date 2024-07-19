from proiect_package1 import tasks

file_path = 'output.txt'  # Specify the correct file path
with open(file_path, 'r') as file:
    tasks.one(file)