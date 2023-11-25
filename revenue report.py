import tkinter as tk
from tkinter import messagebox

class RevenueReportGUI:
    def __init__(self, master, event_registration):
        self.master = master
        self.event_registration = event_registration

        self.calculate_revenue_button = tk.Button(master, text="Calculate Revenue", command=self.calculate_revenue)
        self.calculate_revenue_button.grid(row=0, column=0, pady=10)

    def calculate_revenue(self):
        # Calculate and display revenue report
        total_revenue = self.event_registration.calculate_revenue()
        messagebox.showinfo("Revenue Report", f"Total Revenue from Registrations: ${total_revenue:.2f}")

if __name__ == "__main__": 
    root = tk.Tk()
    revenue_report_gui = RevenueReportGUI(root)
    root.mainloop()
