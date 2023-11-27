# modify_event.py

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from homepage import *
import copy
from create_event import *

def modify_event_window(root, events):
    modify_event_window = tk.Toplevel(root)
    modify_event_window.title("Modify Event")

    event_listbox = tk.Listbox(modify_event_window)
    for event in events:
        event_listbox.insert(END, event.get_name())

    event_listbox.pack(pady=10)

    select_button = tk.Button(modify_event_window, text="Select Event", command=lambda: select_event(events, event_listbox, modify_event_window))
    select_button.pack(pady=10)

def select_event(events, event_listbox, modify_event_window):
    selected_event_index = event_listbox.curselection()

    if not selected_event_index:
        messagebox.showwarning("Warning", "Please select an event.")
        return

    selected_event_index = selected_event_index[0]
    selected_event = events[selected_event_index]

    show_event_details(selected_event, event_listbox, modify_event_window,events)


def show_event_details(selected_event, event_listbox, modify_event_window,events):


    event_details_window = tk.Toplevel(modify_event_window)
    event_details_window.title("Event Details")

    name_label = tk.Label(event_details_window, text=f"Event Name: {selected_event.get_name()}")
    name_label.pack(pady=10)

    date_label = tk.Label(event_details_window, text=f"Event Date: {selected_event.get_start_date()} to {selected_event.get_end_date()}")
    date_label.pack(pady=10)

    desc_label = tk.Label(event_details_window, text=f"Event Description: {selected_event.get_description()}")
    desc_label.pack(pady=10)

    desc_label = tk.Label(event_details_window, text=f"Number of booths: {selected_event.get_booth_amount()}")
    desc_label.pack(pady=10)

    # Add Entry widgets for modifying details
    modify_name_label = tk.Label(event_details_window, text="Modify Event Name:")
    modify_name_label.pack(pady=5)
    modify_name_entry = tk.Entry(event_details_window)
    modify_name_entry.pack(pady=5)

    modify_start_date_label = tk.Label(event_details_window, text="Modify Start Date (MM/DD/YYYY):")
    modify_start_date_label.pack(pady=5)
    modify_start_date_entry = tk.Entry(event_details_window)
    modify_start_date_entry.pack(pady=5)

    modify_end_date_label = tk.Label(event_details_window, text="Modify End Date (MM/DD/YYYY):")
    modify_end_date_label.pack(pady=5)
    modify_end_date_entry = tk.Entry(event_details_window)
    modify_end_date_entry.pack(pady=5)

    modify_desc_label = tk.Label(event_details_window, text="Modify Event Description:")
    modify_desc_label.pack(pady=5)
    modify_desc_entry = tk.Entry(event_details_window)
    modify_desc_entry.pack(pady=5)

    modify_booth_amount_label = tk.Label(event_details_window, text="Modify Amount of Booths:")
    modify_booth_amount_label.pack(pady=5)
    modify_booth_amount_entry = tk.Entry(event_details_window)
    modify_booth_amount_entry.pack(pady=5)

    modify_button = tk.Button(event_details_window, text="Modify Event", command=lambda: modify_event(selected_event, modify_name_entry, modify_start_date_entry, modify_end_date_entry, modify_desc_entry, modify_booth_amount_entry, event_listbox, events, event_details_window, modify_event_window))
    modify_button.pack(pady=10)

    # Add a button to delete the event
    delete_button = tk.Button(event_details_window, text="Delete Event", command=lambda: delete_event(selected_event, event_listbox, events, event_details_window, modify_event_window))
    delete_button.pack(pady=10)

def delete_event(selected_event, event_listbox, events, event_details_window, modify_event_window):
    response = messagebox.askyesno("Delete Event", "Are you sure you want to delete this event?")

    if response == 'yes':
        # Delete the event from the events list
        events.remove(selected_event)

        # Update the event listbox
        event_listbox.delete(event_listbox.curselection())

        messagebox.showinfo("Success", "Event deleted successfully.")

        # Close the event_details_window
        event_details_window.destroy()

        # Close the modify_event_window
        modify_event_window.destroy()

def modify_event(selected_event, modify_name_entry, modify_start_date_entry, modify_end_date_entry, modify_desc_entry, modify_booth_amount_entry, event_listbox,events,event_details_window, modify_event_window):
    modified_event = copy.deepcopy(selected_event)

    # Get modified details from Entry widgets
    new_name = modify_name_entry.get()
    new_start_date = modify_start_date_entry.get()
    new_end_date = modify_end_date_entry.get()
    new_desc = modify_desc_entry.get()
    new_booth_amount = modify_booth_amount_entry.get()

    if new_start_date and not validate_date(new_start_date):
        messagebox.showinfo("Warning", "Please enter date in month/day/year format. Example: 12/01/1999.")
        return

    if new_end_date and not validate_date(new_end_date):
        messagebox.showinfo("Warning", "Please enter date in month/day/year format. Example: 12/01/1999.")
        return

    if new_start_date > new_end_date:
        messagebox.showinfo("Warning", "The start date cannot be later than the end date.")
        return

    # Get selected event index
    selected_event_indices = event_listbox.curselection()
    print(selected_event_indices)

    if not selected_event_indices:
        messagebox.showwarning("Warning", "Please select an event.")
        return


   # Update event details if new information is provided
    if new_name:
        modified_event.set_name(new_name)
    if new_start_date:
        modified_event.set_start_date(new_start_date)
    if new_end_date:
        modified_event.set_end_date(new_end_date)
    if new_desc:
        modified_event.set_description(new_desc)
    if new_booth_amount:
        selected_event.set_booth_amount(new_booth_amount)

    selected_event_index = selected_event_indices[0]

    # Update the event details in the listbox
    events.append(modified_event)
    
    # Remove the original event from the events list
    events.pop(events.index(selected_event))

    messagebox.showinfo("Success", "Event details modified successfully.")

    # Update the event details in the listbox
    event_listbox.insert(END, modified_event.get_name())


    # Close the event_details_window
    event_details_window.destroy()

    # Close the modify_event_window
    modify_event_window.destroy()
