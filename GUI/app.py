import tkinter as tk
from PIL import ImageTk, Image
import os

# Create the main window
root = tk.Tk()

# Set the title and window size
root.title("My App")
root.geometry("640x360")

# Load the background image
image_path = os.path.join("GUI", "Images", "bg.png")
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a welcome message label
welcome_label = tk.Label(root, text="Welcome to My App!", font=("Arial", 20))
welcome_label.pack(pady=20)

# Create the "revision" button
revision_button = tk.Button(root, text="Revision", font=("Arial", 16), command=lambda: os.system("python revision.py"), bd=0, bg="#6ab04c", fg="white", activebackground="#82c983", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, relief="flat", cursor="hand2")
revision_button.place(relx=0.3, rely=0.4, anchor="center")

# Create the "Prepare for exam" button
exam_button = tk.Button(root, text="Prepare for exam", font=("Arial", 16), command=lambda: os.system("python exam.py"), bd=0, bg="#ea7317", fg="white", activebackground="#ff902e", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, relief="flat", cursor="hand2")
exam_button.place(relx=0.7, rely=0.4, anchor="center")

# Start the main loop
root.mainloop()
