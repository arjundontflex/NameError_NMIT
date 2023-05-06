import os
import openai

# Set up OpenAI API key
openai.api_key = "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"

# Define the folder path containing the files
folder_path = "database"

# Define the string to search for
search_string = input("Enter the course name to search for: ")

# Search for all files containing the search string in their name
matching_files = []
for file_name in os.listdir(folder_path):
    if search_string in file_name:
        file_path = os.path.join(folder_path, file_name)
        matching_files.append(file_path)

# Print the matching file paths
if len(matching_files) == 0:
    print(f"No files found containing '{search_string}' in their name.")
else:
    print(f"The following files were found containing '{search_string}' in their name:")
    for file_path in matching_files:
        print(file_path)

# Define the paths to the documents to compare
document1_path = matching_files[0]

# Read in the contents of the documents
with open(document1_path, "r") as f:
    document1 = f.read()

# Initialize the prompt with the first document
prompt = "Match common points between the following documents:\n\nDocument 1:\n" + document1

# Loop over the remaining documents and add them to the prompt
for document_path in matching_files[1:]:
    with open(document_path, "r") as f:
        document = f.read()
    prompt += "\n\nDocument " + str(matching_files.index(document_path)+1) + ":\n" + document

# Add the prompt ending and parameters for the OpenAI API request
prompt += "\n\nMatched points:"
params = {
    "engine": "text-davinci-002",
    "prompt": prompt,
    "temperature": 0.7,
    "max_tokens": 2048,
    "stop": "Matched points:",
}

# Send the request to the OpenAI API
response = openai.Completion.create(**params)

# Extract the matched points from the OpenAI API response
matched_points = response.choices[0].text.strip()

# Split the matched points into a list
matched_points_list = matched_points.split("\n")

# Print out the matched points
print("\nMatched Points:\n")
for point in matched_points_list:
    print(point)
