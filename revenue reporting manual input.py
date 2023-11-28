import tkinter as tk
from tkinter import messagebox

# Define predefined prices for each category
category_prices = {
    "Registration (Observer)": 50.0,
    "Registration (Speaker)": 100.0,
    "Registration (Exhibitor)": 150.0,
    "Other": 0.0,
}

def generate_revenue_report():
    category_revenues = {}
    for category, var in revenue_var_dict.items():
        selected_option = var.get()
        if not selected_option.isdigit():
            messagebox.showwarning("Warning", f"Please select a valid number for {category}.")
            return
        quantity = float(selected_option)
        category_revenues[category] = quantity * category_prices[category]

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
root.title("Revenue Reporter")

# Create and place widgets for revenue (excluding "Sponsorship", "Tickets", and "Merchandise")
revenue_categories = list(category_prices.keys())
revenue_var_dict = {}

for i, category in enumerate(revenue_categories):
    label = tk.Label(root, text=f"{category}:")
    var = tk.StringVar(root)
    var.set("0")  # Default quantity is set to 0

    # If the category is in the "Registration" section, create a single entry widget
    if "Registration" in category:
        options = [str(i) for i in range(51)]  # Numbers from 0 to 50 for quantity
    else:
        options = [str(i) for i in range(51)]  # Numbers from 0 to 50 for quantity

    option_menu = tk.OptionMenu(root, var, *options)

    revenue_var_dict[category] = var

    label.grid(row=i, column=0, padx=10, pady=5, sticky="w")
    option_menu.grid(row=i, column=1, padx=10, pady=5)

revenue_generate_button = tk.Button(root, text="Generate Revenue Report", command=generate_revenue_report)
revenue_generate_button.grid(row=len(revenue_categories), column=0, columnspan=2, pady=10)

revenue_report_text = tk.Text(root, height=10, width=40, state=tk.DISABLED)
revenue_report_text.grid(row=len(revenue_categories) + 1, column=0, columnspan=2, padx=10, pady=10)

# Start the main event loop
root.mainloop()
