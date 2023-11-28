import tkinter as tk
from tkinter import ttk, messagebox

def generate_participant_report():
    category_counts = {}
    total_participants = 0

    for category, combobox in category_comboboxes.items():
        count = combobox.get()
        if not count.isdigit():
            messagebox.showwarning("Warning", "Please select a valid number for each category.")
            return

        count = int(count)
        category_counts[category] = count
        total_participants += count

    # Process the information for the participant report 
    participant_result = "Participant Counts Report:\n\n"
    for category, count in category_counts.items():
        participant_result += f"{category}: {count} participants\n"

    participant_result += f"\nTotal Participants: {total_participants}"

    # Display the participant report
    participant_report_text.config(state=tk.NORMAL)  
    participant_report_text.delete(1.0, tk.END)  
    participant_report_text.insert(tk.END, participant_result)  
    participant_report_text.config(state=tk.DISABLED)  

root = tk.Tk()
root.title("Participants Reporter")

# Create and place widgets for participant counts using dropdown boxes with a range from 0 to 50
participant_categories = ["Exhibitors", "Observers", "Speakers"]
category_comboboxes = {}
for i, category in enumerate(participant_categories):
    label = tk.Label(root, text=f"{category}:")
    combobox_var = tk.StringVar()
    combobox = ttk.Combobox(root, textvariable=combobox_var, values=[str(i) for i in range(51)], state="readonly")
    category_comboboxes[category] = combobox_var

    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    combobox.grid(row=i, column=1, padx=10, pady=5)

participant_generate_button = tk.Button(root, text="Generate Participant Report", command=generate_participant_report)
participant_generate_button.grid(row=len(participant_categories), column=0, columnspan=2, pady=10)

participant_report_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
participant_report_text.grid(row=len(participant_categories) + 1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
