#### Event GUI ###
import tkinter as tk
from tkinter import messagebox
from homepage import *
from authenication import *

# Event Organization Staff Login System

#staff_credentials = {'username': 'one', 'password': '2'}  # Replace with your own credentials

# Create the main application window
root = tk.Tk()
root.title("Event Organizer Login")

# Create and configure labels and entry fields for username and password
username_label = tk.Label(root, text="Username:")
username_label.pack(pady=10)
username_entry = tk.Entry(root)
username_entry.pack(pady=10)

# create and configure labels and entry fields for password
password_label = tk.Label(root, text="Password:")
password_label.pack(pady=10)
password_entry = tk.Entry(root, show="*")  # Show "*" for password entry
password_entry.pack(pady=10)


# Create a button to perform login
login_button = tk.Button(root, text="Login", command= lambda:handle_login(username_entry,password_entry,root))
login_button.pack(pady=10)

# Create a button to open the registration window
register_button = tk.Button(root, text="Register", command= lambda:open_registration_window(root))
register_button.pack(pady=10)

#Create a button to open forgotten username/login window
forgot_button = tk.Button(root,text = "Forgot password or username", command=lambda:open_forgotten_window(root))
forgot_button.pack(pady=10)

# Start the main event loop
root.mainloop()
