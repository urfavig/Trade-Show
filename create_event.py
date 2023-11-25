#create_event.py
#Collects information from the use for the creation of the event
import tkinter as tk
import datetime
from tkinter import messagebox
from homepage import *
from event import *


def create_event_window(root,events):
    global new_event_window
    create_event_window = tk.Toplevel()
    create_event_window.title("Create Event")

    # Entry for event name
    name_label = tk.Label(create_event_window, text="Event Name:")
    name_label.pack(pady=10)
    name_entry = tk.Entry(create_event_window)
    name_entry.pack(pady=10)

    # Entry for event start date
    start_date_label = tk.Label(create_event_window, text="Event start Date:")
    start_date_label.pack(pady=10)
    start_date_entry = tk.Entry(create_event_window)
    start_date_entry.pack(pady=10)

    # Entry for event end date
    end_date_label = tk.Label(create_event_window, text="Event END Date:")
    end_date_label.pack(pady=10)
    end_date_entry = tk.Entry(create_event_window)
    end_date_entry.pack(pady=10)

    # Entry for event description
    desc_label = tk.Label(create_event_window, text="Event Description:")
    desc_label.pack(pady=10)
    desc_entry = tk.Entry(create_event_window)
    desc_entry.pack(pady=10)

    booth_label = tk.Label(create_event_window, text="Number of booths")
    booth_label.pack(pady=10)
    booth_entry = tk.Entry(create_event_window)
    booth_entry.pack(pady=10)


    # Button to create the event
    create_button = tk.Button(create_event_window, text="Create Event", command=lambda:create_event(name_entry.get(), start_date_entry.get(),end_date_entry.get(), desc_entry.get(),booth_entry.get()))
    create_button.pack(pady=10)

    def create_event(name, start_date, end_date, description,booths):
        if (validate_date(start_date) and validate_date(end_date)):
            try:
                # Create an Event object or perform necessary actions with the event details
                new_event = Event(name, start_date,end_date ,description,booths)
                messagebox.showinfo("Success","The event " + name + " has been created." )
                print(f"Event Created: {new_event.get_event_details()}")
            except Exception as e:
                # Display an error message if event creation fails
                events.append(new_event)
                messagebox.showerror("Error", f"Failed to create event. Error: {str(e)}")
        else:
            messagebox.showinfo("Please enter date in month/day/year format please." )
            

    #validates the entry date
    def validate_date(date):
        try:
            # Try to parse the date string
            datetime.datetime.strptime(date, '%m/%d/%Y')
            return True
        except ValueError:
            return False
        
    
