# homepage.py

import tkinter as tk


#Opens the homepage for the event
def open_homepage(username):
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

