import os

# define the folder path containing the files
folder_path = "database"

# define the string to search for
search_string = input("Enter the string to search for: ")

# search for all files containing the search string in their name
matching_files = []
for file_name in os.listdir(folder_path):
    if search_string in file_name:
        file_path = os.path.join(folder_path, file_name)
        matching_files.append(file_path)

# print the matching file paths
if len(matching_files) == 0:
    print(f"No files found containing '{search_string}' in their name.")
else:
    print(f"The following files were found containing '{search_string}' in their name:")
    for file_path in matching_files:
        print(file_path)
