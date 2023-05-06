import tkinter as tk
from tkinter import *  
from tkinter import messagebox
import os
from PIL import Image, ImageTk

class UserAuth:
    def __init__(self, master):
        self.master = master
        master.title("User Authentication")
        self.base_folder = "datasets" 
        master.geometry("800x450")

        # Load the background image
        bg_image = Image.open("GUI\Images\\back.jpg")
        bg_photo = ImageTk.PhotoImage(bg_image)

        # Create a label for the background image and add it to the window
        self.bg_label = tk.Label(master, image=bg_photo)
        self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Make sure to keep a reference to the image to prevent it from being garbage collected
        self.bg_label.image = bg_photo

        # Create a label and buttons for signing in and signing up
        self.label = tk.Label(master, text="Choose an option:")
        self.label.pack()
        
        # Customize the font and size of the buttons
        button_font = ("Arial", 12)
        button_width = 10
        button_height = 2

        self.signup_button = tk.Button(master, text="Sign Up", command=self.signup, font=button_font, width=button_width, height=button_height)
        self.signup_button.pack()
        
        self.signin_button = tk.Button(master, text="Sign In", command=self.signin, font=button_font, width=button_width, height=button_height)
        self.signin_button.pack()
        
        
        # Place the buttons at the center of the window
        self.signup_button.place(x=350, y=200)
        self.signin_button.place(x=350, y=300)

    def signup(self):
        # Create a new window for signing up
        self.signup_window = tk.Toplevel(self.master)
        self.signup_window.title("Sign Up")
        self.signup_window.geometry("500x300")

        # Create entry fields for the username and password
        self.username_label = tk.Label(self.signup_window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.signup_window)
        self.username_entry.pack()
        self.password_label = tk.Label(self.signup_window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.signup_window, show="*")
        self.password_entry.pack()

        # Create a button to submit the form
        self.submit_button = tk.Button(self.signup_window, text="Submit", command=self.create_folder)
        self.submit_button.pack()

    def create_folder(self):
        # Get the username and password from the entry fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Create a new folder for the user
        user_folder = os.path.join(os.getcwd(), "Datasets",username)
        if not os.path.exists(user_folder):
            os.makedirs(user_folder)

        # Save the password in a file in the user's folder
        password_file = os.path.join(user_folder, "password.txt")
        with open(password_file, "w") as f:
            f.write(password)

        # Show a message indicating that the sign up was successful
        messagebox.showinfo("Sign Up Complete", "Your account has been created.")

        # Close the sign up window
        self.signup_window.destroy()

    def signin(self):
        # Create a new window for signing in
        self.signin_window = tk.Toplevel(self.master)
        self.signin_window.title("Sign In")
        self.signin_window.geometry("500x300")

        # Create entry fields for the username and password
        self.username_label = tk.Label(self.signin_window, text="Username:")
        self.username_label.pack()
        self.username_entry = tk.Entry(self.signin_window)
        self.username_entry.pack()
        self.password_label = tk.Label(self.signin_window, text="Password:")
        self.password_label.pack()
        self.password_entry = tk.Entry(self.signin_window, show="*")
        self.password_entry.pack()

        # Create a button to submit the form
        self.submit_button = tk.Button(self.signin_window, text="Submit", command=self.show_folder)
        self.submit_button.pack()

    def show_folder(self):
        # Get the username and password from the input fields
        username = self.username_entry.get()
        password = self.password_entry.get()

        # Check if the username exists
        user_folder = os.path.join(self.base_folder, username)
        if os.path.isdir(user_folder):
            # Check if the password is correct
            password_file = os.path.join(user_folder, "password.txt")
            with open(password_file, "r") as f:
                saved_password = f.read()
            if password == saved_password:
                # Execute the Python code if the password is correct
                os.system("python GUI\\app.py")

                # Close the tkinter window
                self.root.destroy()

            else:
                # Show an error message if the password is incorrect
                messagebox.showerror("Error", "Incorrect password.")
        else:
            # Show an error message if the username doesn't exist
            messagebox.showerror("Error", "Username not found.")
root = tk.Tk()
auth = UserAuth(root)
root.mainloop()