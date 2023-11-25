import tkinter as tk
from tkinter import messagebox

def generate_revenue_report():
    category_revenues = {}
    for category, entry_var in revenue_entries.items():
        revenue = entry_var.get()
        if not revenue.replace('.', '').isdigit():
            messagebox.showwarning("Warning", "Please enter a valid number for each category.")
            return
        category_revenues[category] = float(revenue)

    # Calculate total revenue
    total_revenue = sum(category_revenues.values())

    # Process the information for the revenue report (replace this with your actual logic)
    revenue_result = "Revenue Report:\n\n"
    for category, revenue in category_revenues.items():
        revenue_result += f"{category}: ${revenue:.2f}\n"

    revenue_result += f"\nTotal Revenue: ${total_revenue:.2f}"

    # Display the revenue report
    revenue_report_text.config(state=tk.NORMAL)  # Enable text widget for editing
    revenue_report_text.delete(1.0, tk.END)  # Clear previous content
    revenue_report_text.insert(tk.END, revenue_result)  # Insert the new report
    revenue_report_text.config(state=tk.DISABLED)  # Disable text widget for editing

# Create the main window
root = tk.Tk()
root.title("Revenue Report Generator")

# Create and place widgets for revenue
revenue_categories = ["Tickets", "Merchandise", "Sponsorship", "Registrations", "Other"]
revenue_entries = {}
for i, category in enumerate(revenue_categories):
    label = tk.Label(root, text=f"{category} ($):")
    entry_var = tk.StringVar()
    entry = tk.Entry(root, textvariable=entry_var)
    revenue_entries[category] = entry_var

    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    entry.grid(row=i, column=1, padx=10, pady=5)

revenue_generate_button = tk.Button(root, text="Generate Revenue Report", command=generate_revenue_report)
revenue_generate_button.grid(row=len(revenue_categories), column=0, columnspan=2, pady=10)

revenue_report_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
revenue_report_text.grid(row=len(revenue_categories) + 1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
