# homepage.py

import tkinter as tk
from tkinter import *
from event import *
from create_event import *
<<<<<<< HEAD
from modify_event import modify_event_window

=======
from MainApplication import *
>>>>>>> 803d7871e6607639349637c446354625999c1483


#Opens the homepage for the event
def open_homepage(username):
    global homepage_window
    homepage_window = tk.Toplevel()
    homepage_window.title("Event Organizer Homepage")

    # List to store created events
    events = []

    welcome_label = tk.Label(homepage_window, text=f"Welcome, {username}!")
    welcome_label.pack(pady=20)

    create_event_button = tk.Button(homepage_window, text = "Create new event", command=lambda:create_event_window(homepage_window,events))
    create_event_button.pack(pady= 10)

    register_guest_button = tk.Button(homepage_window, text = "Register Guest", command=lambda:open_registration_window())
    register_guest_button.pack(pady=10)

    manage_events_button = tk.Button(homepage_window,text="Manage Events",command=lambda: modify_event_window(homepage_window, events))
    manage_events_button.pack(pady=10)

    logout_button = tk.Button(homepage_window,text= "Logout", command=lambda:homepage_window.destroy())
    logout_button.pack(pady = 10)

