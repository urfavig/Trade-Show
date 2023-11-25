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
    create_button = tk.Button(create_event_window, text="Create Event", command=lambda:create_event(name_entry.get(), start_date_entry.get(),end_date_entry.get(), desc_entry.get(), booth_entry.get()))
    create_button.pack(pady=10)

    def create_event(name, start_date, end_date, description, booth_amount):
        if not (validate_date(start_date) and validate_date(end_date)):
            messagebox.showinfo("Warning", "Please enter date in month/day/year format. Example: 12/01/1999.")
            return  # Exit the function if the dates are not valid

        start_date_obj = datetime.datetime.strptime(start_date, '%m/%d/%Y')
        end_date_obj = datetime.datetime.strptime(end_date, '%m/%d/%Y')
        if start_date_obj > end_date_obj:
            messagebox.showwarning("Warning", "The start date cannot be later than the end date.")
            return

        if not booth_amount.isdigit():
            messagebox.showwarning("Warning", "You must put in a numerical value for the booths.")
            return

        try:
            # Create an Event object
            new_event = Event(name, start_date, end_date, description, booth_amount)
        
            # Append the event to the list after successful creation
            events.append(new_event)

            # Display success message
            messagebox.showinfo("Success", "The event " + name + " has been created.")
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
