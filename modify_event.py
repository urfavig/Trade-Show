# modify_event.py

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from event import Event  # Assuming Event class is defined in the event.py file

def modify_event_window(root, events):
    global modify_event_window
    modify_event_window = tk.Toplevel()
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

    show_event_details(selected_event, event_listbox, modify_event_window)

def show_event_details(selected_event, event_listbox, modify_event_window):
    event_details_window = tk.Toplevel()
    event_details_window.title("Event Details")

    name_label = tk.Label(event_details_window, text=f"Event Name: {selected_event.get_name()}")
    name_label.pack(pady=10)

    date_label = tk.Label(event_details_window, text=f"Event Date: {selected_event.get_date()}")
    date_label.pack(pady=10)

    desc_label = tk.Label(event_details_window, text=f"Event Description: {selected_event.get_description()}")
    desc_label.pack(pady=10)

    modify_desc_label = tk.Label(event_details_window, text="Modify Description:")
    modify_desc_label.pack(pady=10)

    modify_desc_entry = tk.Entry(event_details_window, width=50)
    modify_desc_entry.pack(pady=10)

    modify_desc_button = tk.Button(event_details_window, text="Modify Description", command=lambda: modify_description(selected_event, modify_desc_entry, event_listbox))
    modify_desc_button.pack(pady=10)

def modify_description(selected_event, new_description, event_listbox):
    new_description_text = new_description.get()
    selected_event.set_description(new_description_text)
    
    # Update the event description in the listbox
    selected_event_index = event_listbox.curselection()[0]
    event_listbox.delete(selected_event_index)
    event_listbox.insert(selected_event_index, selected_event.get_name())

    messagebox.showinfo("Success", "Event description modified successfully.")

# Example usage
if __name__ == "__main__":
    # Assuming 'events' is a list of Event objects
    events = [Event("Event1", "2023-01-01", "2023-01-10", "Description1", 10),
              Event("Event2", "2023-02-01", "2023-02-10", "Description2", 15)]

    root = tk.Tk()
    modify_event_window(root, events)
    root.mainloop()
