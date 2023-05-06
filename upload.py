import tkinter as tk
from tkinter import filedialog
import shutil

# Create the tkinter window
root = tk.Tk()
root.title("File Uploader")

# Function to handle the file upload
def upload_file():
    # Open a file dialog to select the file to upload
    file_path = filedialog.askopenfilename()
    # Copy the selected file to the database path
    shutil.copy(file_path, "database")

# Create the upload button
upload_button = tk.Button(root, text="Upload File", command=upload_file)
upload_button.pack()

# Run the tkinter event loop
root.mainloop()
