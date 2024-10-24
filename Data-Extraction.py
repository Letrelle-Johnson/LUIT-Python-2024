# Importing os module 
import os

# Retrieve current working directory path
current_dir = os.getcwd()

# List all items for both files and directories from the current directory 
all_items = os.listdir(current_dir)

file_list_info = []

def reveal_file_info():
    # Create an empty file to conceal info about files
    file_list_info = []
    # Loop items in directory 
    for item in all_items:
        # Show full path of each item
        full_path = os.path.join(current_dir, item)

        # Confirm the item is a file and not directory
    if os.path.isfile(full_path):
        file_info = {
            'file_size': os.path.getsize(full_path),
            'file_path': full_path
        }

        # Include file info to the list
        file_list_info.append(file_info)

for info in file_list_info:
    print(reveal_file_info)