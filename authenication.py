# authentication.py

import tkinter as tk
from tkinter import messagebox
from homepage import *

#Saved usernames and passowords or users
staff_credentials = {'one':'two'}

#Checks to see if username and password is valid
def login(username, password):
     return username in staff_credentials and password == staff_credentials[username]

#Handles the login of a user and opens homepage
def handle_login(username_entry, password_entry, root):
    entered_username = username_entry.get()
    entered_password = password_entry.get()

    if login(entered_username, entered_password):
        root.withdraw()
        open_homepage(entered_username)
    else:
        messagebox.showerror("Login Failed", "Invalid username or password. Please try again.")

#Adds the new user to staff_credentials
def register_user(new_username_entry, new_password_entry ,email_entry, registration_window):
    new_username = new_username_entry.get()
    new_password = new_password_entry.get()
    email = email_entry.get()

    if new_username and new_password:
        staff_credentials[new_username] = new_password
        staff_credentials[email] = new_username
        messagebox.showinfo("Registration Successful", "User registered successfully!")
        print(staff_credentials)
        registration_window.destroy()  # Close the registration window after successful registration
    else:
        messagebox.showerror("Registration Failed", "Please enter both username and password.")


#Opens a registration windoe
def open_registration_window(root):
    global registration_window
    registration_window = tk.Toplevel(root)
    registration_window.title("User Registration")

    #Entry for new username
    new_username_label = tk.Label(registration_window, text="New Username:")
    new_username_label.pack(pady=10)
    new_username_entry = tk.Entry(registration_window)
    new_username_entry.pack(pady=10)


    #Entry for new password
    new_password_label = tk.Label(registration_window, text="New Password:")
    new_password_label.pack(pady=10)
    new_password_entry = tk.Entry(registration_window, show="*")
    new_password_entry.pack(pady=10)

    #create and configure labels and entry fields for email
    email_label = tk.Label(registration_window,text= "Email")
    email_label.pack(pady=10)
    email_entry = tk.Entry(registration_window)
    email_entry.pack(pady = 10)

    #Button to complete
    register_user_button = tk.Button(registration_window, text="Register", command=lambda: register_user(new_username_entry, new_password_entry,email_entry, registration_window))
    register_user_button.pack(pady=10)

#Open account recovery window
def open_forgotten_window(root):

    #Creates a widow for the user to recover account 
    global forgotten_window
    forgotten_window = tk.Toplevel(root)
    forgotten_window.title("Forgotten passowrd or username")
    forgotten_label = tk.Label(forgotten_window,text= "Please enter the email associated with your account")
    forgotten_label.pack(pady=10)
    forgotten_entry = tk.Entry(forgotten_window)
    forgotten_entry.pack(pady = 10)

    #button to send email to associated account
    send_email_button = tk.Button(forgotten_window,text="Send emaill to recover account",command=lambda:validate_email(forgotten_entry))
    send_email_button.pack(pady=10)

    #Destroys window after a email has been entered
    #forgotten_window.destroy()


def check_email(email):
     return email in staff_credentials

#Handles the login of a user and opens homepage
def validate_email(forgotten_entry):
    forgotten_email = forgotten_entry.get()

    messagebox.showinfo("Complete","If a email is asssociated with the email a recovery email has been sent")

    forgotten_window.destroy()
