import tkinter as tk
from PIL import ImageTk, Image
import os

# Create the main window
root = tk.Tk()

# Set the title and window size
root.title("My App")
root.geometry("800x600")

# Load the background image
image_path = os.path.join("GUI", "Images", "bg4.jpg")
image = Image.open(image_path)
background_image = ImageTk.PhotoImage(image)

# Create a label with the background image
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Create a welcome message label
welcome_label = tk.Label(root, text="Welcome", font=("Arial", 20), bg='white', fg='black')
welcome_label.pack(pady=20)
welcome_label.place(x=360, y=90)

# Create the "revision" button
revision_button = tk.Button(root, text="Revision", font=("Arial", 16), command=lambda: os.system("python revision.py"), bd=0, bg="skyblue", fg="black", activebackground="#82c983", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, relief="groove", cursor="hand2")
revision_button.place(relx=0.5, rely=0.3, anchor="center")
# Place the buttons
revision_button.place(x=20, y=100)


# Create the "Prepare for exam" button
exam_button = tk.Button(root, text="Prepare for exam", font=("Arial", 16), command=lambda: os.system("python exam.py"), bd=0, bg="#ea7317", fg="white", activebackground="#ff902e", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, relief="groove", cursor="hand2")
exam_button.place(relx=0.5, rely=0.4, anchor="center")
exam_button.place(x=20, y=150)

# Create the "exit" button
exit_button = tk.Button(root, text="Exit", font=("Arial", 16), command=root.destroy, bd=0, bg="red", fg="white", activebackground="#333333", activeforeground="white", padx=20, pady=10, borderwidth=0, highlightthickness=0, relief="groove", cursor="hand2")
exit_button.place(relx=0.95, rely=0.9, anchor="center")

# Start the main loop
root.mainloop()
