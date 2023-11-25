# modify_event.py

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from homepage import *
import copy

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

    modify_button = tk.Button(event_details_window, text="Modify Event", command=lambda: modify_event(selected_event, modify_name_entry, modify_start_date_entry, modify_end_date_entry, modify_desc_entry, event_listbox,events,event_details_window,modify_event_window))
    modify_button.pack(pady=10)

def modify_event(selected_event, modify_name_entry, modify_start_date_entry, modify_end_date_entry, modify_desc_entry, event_listbox,events,event_details_window,modify_event_window):
    modified_event = copy.deepcopy(selected_event)

    # Get modified details from Entry widgets
    new_name = modify_name_entry.get()
    new_start_date = modify_start_date_entry.get()
    new_end_date = modify_end_date_entry.get()
    new_desc = modify_desc_entry.get()

    # Get selected event index
    selected_event_indices = event_listbox.curselection()

    if not selected_event_indices:
        messagebox.showwarning("Warning", "Please select an event.")
        return

    selected_event_index = selected_event_indices[0]

   # Update event details if new information is provided
    if new_name:
        modified_event.set_name(new_name)
    if new_start_date:
        modified_event.set_start_date(new_start_date)
    if new_end_date:
        modified_event.set_end_date(new_end_date)
    if new_desc:
        modified_event.set_description(new_desc)

    # Update the event details in the listbox
    events.append(modified_event)

    # Update the event details in the listbox
    event_listbox.insert(END, modified_event.get_name())

    messagebox.showinfo("Success", "Event details modified successfully.")

    # Remove the original event from the events list
    events.pop(events.index(selected_event))

    # Close the event_details_window
    event_details_window.destroy()

    # Close the event_details_window
    modify_event_window.destroy()
