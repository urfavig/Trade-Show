# homepage.py

import tkinter as tk
from event import *


#Opens the homepage for the event
def open_homepage(username):
    global homepage_window
    homepage_window = tk.Toplevel()
    homepage_window.title("Event Organizer Homepage")

    welcome_label = tk.Label(homepage_window, text=f"Welcome, {username}!")
    welcome_label.pack(pady=20)

    create_event_button = tk.Button(homepage_window, text = "Create new event")
    create_event_button.pack(pady= 10)

    register_guest_button = tk.Button(homepage_window, text = "register guest")
    register_guest_button.pack(pady=10)

    manage_events_button = tk.Button(homepage_window,text="Manage Events")
    manage_events_button.pack(pady=10)

    logout_button = tk.Button(homepage_window,text= "Logout", command=lambda:homepage_window.destroy())
    logout_button.pack(pady = 10)

def create_event_window():
    global new_event_window
    registration_window = tk.Toplevel(homepage_window)
    registration_window.title("User Registration")

    #Entry for new username
    event_name_label = tk.Label(registration_window, text="New Username:")
    event_name_label.pack(pady=10)
    event_name_entry = tk.Entry(registration_window)
    event_name_entry.pack(pady=10)


    #Entry for new password
    date_label = tk.Label(registration_window, text="New Password:")
    date_label.pack(pady=10)
    date_entry = tk.Entry(registration_window, show="*")
    date_entry.pack(pady=10)

    #create and configure labels and entry fields for email
    desc_label = tk.Label(registration_window,text= "Email")
    desc_label.pack(pady=10)
    desc_entry = tk.Entry(registration_window)
    desc_entry.pack(pady = 10)

    #Button to complete
    creation_button = tk.Button(registration_window, text="Register", command=lambda: ())
    creation_button.pack(pady=10)