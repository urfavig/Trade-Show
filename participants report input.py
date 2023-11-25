import tkinter as tk
from tkinter import messagebox

def generate_participant_report():
    category_counts = {}
    total_participants = 0

    for category, entry_var in category_entries.items():
        count = entry_var.get()
        if not count.isdigit():
            messagebox.showwarning("Warning", "Please enter a valid number for each category.")
            return

        count = int(count)
        category_counts[category] = count
        total_participants += count

    # Process the information for the participant report (replace this with your actual logic)
    participant_result = "Participant Counts Report:\n\n"
    for category, count in category_counts.items():
        participant_result += f"{category}: {count} participants\n"

    participant_result += f"\nTotal Participants: {total_participants}"

    # Display the participant report
    participant_report_text.config(state=tk.NORMAL)  # Enable text widget for editing
    participant_report_text.delete(1.0, tk.END)  # Clear previous content
    participant_report_text.insert(tk.END, participant_result)  # Insert the new report
    participant_report_text.config(state=tk.DISABLED)  # Disable text widget for editing

root = tk.Tk()
root.title("Participants Reporter")

# Create and place widgets for participant counts
participant_categories = ["Exhibitors", "Observers", "Speakers"]
category_entries = {}
for i, category in enumerate(participant_categories):
    label = tk.Label(root, text=f"{category}:")
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var)
    category_entries[category] = entry_var

    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry.grid(row=i, column=1, padx=10, pady=5)

participant_generate_button = tk.Button(root, text="Generate Participant Report", command=generate_participant_report)
participant_generate_button.grid(row=len(participant_categories), column=0, columnspan=2, pady=10)

participant_report_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
participant_report_text.grid(row=len(participant_categories) + 1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
