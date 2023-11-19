import tkinter as tk
from tkinter import ttk  # Import the ttk module for Notebook
from tkinter import messagebox

class EventRegistration:
    def __init__(self):
        self.exhibitors = []
        self.speakers = []
        self.observers = []
        self.registration_counter = 0

    def register_exhibitor(self, name, topic, email, contact_number):
        participant_type = "E"
        if name and topic and email and contact_number:
            self.registration_counter += 1
            registration_number = self.generate_registration_number(participant_type)
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

    def register_speaker(self, name, topic, email, contact_number):
        participant_type = "S"
        if name and topic and email and contact_number:
            self.registration_counter += 1
            registration_number = self.generate_registration_number(participant_type)
            speaker_info = {
                'Registration Number': registration_number,
                'Name': name,
                'Topic': topic,
                'Email': email,
                'Contact Number': contact_number
            }
            self.speakers.append(speaker_info)
            return f"Speaker {name} successfully registered with Registration Number {registration_number}"
        else:
            return "Error: Insufficient data provided. Please provide all required information."

    def register_observer(self, name, topic, email, contact_number):
        participant_type = "O"
        if name and topic and email and contact_number:
            self.registration_counter += 1
            registration_number = self.generate_registration_number(participant_type)
            observer_info = {
                'Registration Number': registration_number,
                'Name': name,
                'Topic': topic,
                'Email': email,
                'Contact Number': contact_number
            }
            self.observers.append(observer_info)
            return f"Observer {name} successfully registered with Registration Number {registration_number}"
        else:
            return "Error: Insufficient data provided. Please provide all required information."

    def generate_registration_number(self):
        return f"{participant_type}-{self.registration_counter:04d}"

class EventRegistrationGUI:
    def __init__(self, master, registration_type, display_text):
        self.master = master
        self.registration_type = registration_type  # Store registration_type in the instance

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

        self.register_button = tk.Button(master, text=f"Register {registration_type}", command=self.register)
        self.register_button.grid(row=4, column=0, columnspan=2, pady=10)

        # Create an instance of EventRegistration to handle the registration logic
        self.event_registration = EventRegistration()

    def register(self):
        name = self.name_entry.get()
        topic = self.topic_entry.get()
        email = self.email_entry.get()
        contact_number = self.contact_entry.get()

        if hasattr(self.event_registration, f"register_{self.registration_type.lower()}"):
            registration_method = getattr(self.event_registration, f"register_{self.registration_type.lower()}")
            registration_result = registration_method(name, topic, email, contact_number)

            # Display registration result in a message box
            messagebox.showinfo("Registration Result", registration_result)
        else:
            messagebox.showerror("Error", f"Registration method for {self.registration_type} not found.")

class MainApplication:
    def __init__(self, master):
        master.title("Event Registration System")

        # Create tabs for each registration type
        notebook = ttk.Notebook(master)  # Use ttk.Notebook for styling
        notebook.pack(fill=tk.BOTH, expand=True)

        exhibitor_tab = tk.Frame(notebook)
        speaker_tab = tk.Frame(notebook)
        observer_tab = tk.Frame(notebook)

        notebook.add(exhibitor_tab, text="Exhibitor Registration")
        notebook.add(speaker_tab, text="Speaker Registration")
        notebook.add(observer_tab, text="Observer Registration")

        # Create instances of EventRegistrationGUI for each type
        exhibitor_registration_gui = EventRegistrationGUI(exhibitor_tab, "Exhibitor", "Exhibitor")
        speaker_registration_gui = EventRegistrationGUI(speaker_tab, "Speaker", "Speaker")
        observer_registration_gui = EventRegistrationGUI(observer_tab, "Observer", "Observer")

        # Create an instance of EventRegistration to handle the registration logic
        event_registration = EventRegistration()

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApplication(root)
    root.mainloop()
