#create_event.py
#Collects information from the use for the creation of the event
import tkinter as tk
import datetime
from tkinter import messagebox
from homepage import *
from event import *
def create_event_window(root):
    global new_event_window
    create_event_window = tk.Toplevel()
    create_event_window.title("Create Event")

    # Entry for event name
    name_label = tk.Label(create_event_window, text="Event Name:")
    name_label.pack(pady=10)
    name_entry = tk.Entry(create_event_window)
    name_entry.pack(pady=10)

    # Entry for event date
    date_label = tk.Label(create_event_window, text="Event Date:")
    date_label.pack(pady=10)
    date_entry = tk.Entry(create_event_window)
    date_entry.pack(pady=10)

    # Entry for event description
    desc_label = tk.Label(create_event_window, text="Event Description:")
    desc_label.pack(pady=10)
    desc_entry = tk.Entry(create_event_window)
    desc_entry.pack(pady=10)

    # Button to create the event
    create_button = tk.Button(create_event_window, text="Create Event", command=lambda:create_event(name_entry.get(), date_entry.get(), desc_entry.get()))
    create_button.pack(pady=10)

    def create_event(name, start_date, end_date, description):
        try:
            # Create an Event object or perform necessary actions with the event details
            new_event = Event(name, start_date,end_date ,description)
            messagebox.showinfo("Success","The event " + name + " has been created." )
            print(f"Event Created: {new_event.get_event_details()}")
        except Exception as e:
            # Display an error message if event creation fails
            messagebox.showerror("Error", f"Failed to create event. Error: {str(e)}")
    #validates the entry date
    def validate_date(date):
        try:
            # Try to parse the date string
            datetime.datetime.strptime(date, '%m/%d/%Y')
            return True
        except ValueError:
            return False
