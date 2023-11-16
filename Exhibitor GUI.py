import tkinter as tk
from tkinter import messagebox

class EventRegistration:
    def __init__(self):
        self.exhibitors = []
        self.registration_counter = 0

    def register_exhibitor(self, name, topic, email, contact_number):
        if name and topic and email and contact_number:
            self.registration_counter += 1
            registration_number = self.generate_registration_number()
            exhibitor_info = {
                'Registration Number': registration_number,
                'Name': name,
                'Topic': topic,
                'Email': email,
                'Contact Number': contact_number
            }
            self.exhibitors.append(exhibitor_info)
            return f"Exhibitor {name} successfully registered with Registration Number {registration_number}"
        else:
            return "Error: Insufficient data provided. Please provide all required information."

    def generate_registration_number(self):
        return f"REG-{self.registration_counter:04d}"


class EventRegistrationGUI:
    def __init__(self, master):
        self.master = master
        master.title("Exhibitor Registration")

        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0, sticky=tk.E)

        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.topic_label = tk.Label(master, text="Topic:")
        self.topic_label.grid(row=1, column=0, sticky=tk.E)

        self.topic_entry = tk.Entry(master)
        self.topic_entry.grid(row=1, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=2, column=0, sticky=tk.E)

        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=2, column=1)

        self.contact_label = tk.Label(master, text="Contact Number:")
        self.contact_label.grid(row=3, column=0, sticky=tk.E)

        self.contact_entry = tk.Entry(master)
        self.contact_entry.grid(row=3, column=1)

        self.register_button = tk.Button(master, text="Register", command=self.register_exhibitor)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=10)

        self.event_registration = EventRegistration()

    def register_exhibitor(self):
        name = self.name_entry.get()
        topic = self.topic_entry.get()
        email = self.email_entry.get()
        contact_number = self.contact_entry.get()

        registration_result = self.event_registration.register_exhibitor(name, topic, email, contact_number)

        # Display registration result in a message box
        messagebox.showinfo("Registration Result", registration_result)

if __name__ == "__main__":
    root = tk.Tk()
    exhibitor_registration_gui = EventRegistrationGUI(root)

    root.mainloop()
