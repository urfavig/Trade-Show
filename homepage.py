# homepage.py

import tkinter as tk
from participent_report import *
from tkinter import *
from event import *
from create_event import *
from MainApplication import *

#Opens the homepage for the event
def open_homepage(username):
    from modify_event import modify_event_window

    global homepage_window
    homepage_window = tk.Toplevel()
    homepage_window.title("Event Organizer Homepage")

    # List to store created events
    events = []
    dummy_event = Event("Test Event", "01/01/2023", "01/10/2023", "Test Description", 10)
    events.append(dummy_event)

    welcome_label = tk.Label(homepage_window, text=f"Welcome, {username}!")
    welcome_label.pack(pady=20)
    
    #Create new event button
    create_event_button = tk.Button(homepage_window, text = "Create new event", command=lambda:create_event_window(homepage_window,events))
    create_event_button.pack(pady= 10)

    #Register guest button
    register_guest_button = tk.Button(homepage_window, text = "Register Guest", command=lambda:open_registration_window())
    register_guest_button.pack(pady=10)

    #Add manage event button
    manage_events_button = tk.Button(homepage_window,text="Manage Events",command=lambda: modify_event_window(homepage_window, events))
    manage_events_button.pack(pady=10)

    #Add revenure button
    event_revenue_button = tk.Button(homepage_window,text="Check Revenue",command=lambda: modify_event_window(homepage_window, events))
    event_revenue_button.pack(pady=10)

    # Add a new button to view participants
    view_participants_button = tk.Button(homepage_window, text="View Participants", command=lambda: summary_window(homepage_window,events))
    view_participants_button.pack(pady=10)

    logout_button = tk.Button(homepage_window,text= "Logout", command=lambda:logout())
    logout_button.pack(pady = 10)

    def logout():
        homepage_window.destroy()
        messagebox.showinfo("Logout","Logout was successful")
