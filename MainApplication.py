import tkinter as tk
from tkinter import ttk, messagebox

class User:
    def __init__(self, username, password, role):
        self.username = username
        self.password = password
        self.role = role

class Participant:
    def __init__(self, registration_number, name, topic, email, contact_number):
        self.registration_number = registration_number
        self.name = name
        self.topic = topic
        self.email = email
        self.contact_number = contact_number

class EventRegistration:
    def __init__(self):
        self.participants = []
        self.registration_counter = 0
        self.used_registration_numbers = set()

    def generate_registration_number(self, participant_type):
        if participant_type == 'participant':
            participant_type = 'P'
        elif participant_type == 'exhibitor':
            participant_type = 'E'
        elif participant_type == 'speaker':
            participant_type = 'S'
        elif participant_type == 'observer':
            participant_type = 'O'
        else:
            return None

        counter = 1
        while True:
            registration_number = f"{participant_type}-{counter:04d}"
            if registration_number not in self.used_registration_numbers:
                self.used_registration_numbers.add(registration_number)
                return registration_number
            counter += 1

    def register_participant(self, name, topic, email, contact_number):
        self.registration_counter += 1
        registration_number = self.generate_registration_number('participant')
        participant = Participant(registration_number, name, topic, email, contact_number)
        self.participants.append(participant)
        return f"Participant {name} successfully registered with Registration Number {registration_number}"

    def get_participant_info(self, registration_number):
        for participant in self.participants:
            if participant.registration_number == registration_number:
                return participant
        return None

    def update_participant(self, registration_number, name, topic, email, contact_number):
        for participant in self.participants:
            if participant.registration_number == registration_number:
                participant.name = name
                participant.topic = topic
                participant.email = email
                participant.contact_number = contact_number
                return f"Participant {name} information updated successfully."

        return f"Participant with Registration Number {registration_number} not found."

    def delete_participant(self, registration_number):
        for participant in self.participants:
            if participant.registration_number == registration_number:
                self.participants.remove(participant)
                self.used_registration_numbers.remove(registration_number)
                return f"Participant with Registration Number {registration_number} deleted successfully."

        return f"Participant with Registration Number {registration_number} not found."

class RoleSelectionGUI:
    def __init__(self, master, on_selection):
        self.master = master
        self.on_selection = on_selection

        self.role_var = tk.StringVar()

        self.label = tk.Label(master, text="Select your role:")
        self.label.pack(pady=10)

        roles = ["Staff Member", "Exhibitor", "Speaker", "Observer"]
        for role in roles:
            tk.Radiobutton(master, text=role, variable=self.role_var, value=role).pack()

        self.continue_button = tk.Button(master, text="Continue", command=self.continue_to_credentials)
        self.continue_button.pack(pady=10)

    def continue_to_credentials(self):
        selected_role = self.role_var.get()
        if selected_role:
            self.on_selection(selected_role)
        else:
            messagebox.showwarning("Role Selection", "Please select a role before continuing.")

class CredentialEntryGUI:
    def __init__(self, master, role, on_credentials_entry):
        self.master = master
        self.role = role
        self.on_credentials_entry = on_credentials_entry

        self.username_label = tk.Label(master, text="Username:")
        self.username_label.pack(pady=10)

        self.username_entry = tk.Entry(master)
        self.username_entry.pack(pady=10)

        self.password_label = tk.Label(master, text="Password:")
        self.password_label.pack(pady=10)

        self.password_entry = tk.Entry(master, show="*")
        self.password_entry.pack(pady=10)

        self.submit_button = tk.Button(master, text="Submit", command=self.submit_credentials)
        self.submit_button.pack(pady=10)

    def submit_credentials(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        self.on_credentials_entry(username, password)

class EventRegistrationGUI:
    def __init__(self, master, registration_type, display_text, current_user):
        self.master = master
        self.registration_type = registration_type
        self.current_user = current_user

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

        self.view_info_button = tk.Button(master, text=f"View {registration_type} Info", command=self.view_info)
        self.view_info_button.grid(row=5, column=0, columnspan=2, pady=10)

        self.update_button = tk.Button(master, text=f"Update {registration_type} Info", command=self.update_info)
        self.update_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.delete_button = tk.Button(master, text=f"Delete {registration_type}", command=self.delete_info)
        self.delete_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.event_registration = EventRegistration()

    def register(self):
        name = self.name_entry.get()
        topic = self.topic_entry.get()
        email = self.email_entry.get()
        contact_number = self.contact_entry.get()

        registration_method = getattr(self.event_registration, f"register_{self.registration_type.lower()}")
        registration_result = registration_method(name, topic, email, contact_number)

        # Display confirmation overview
        confirmation_message = f"{self.registration_type} Details:\n" \
                               f"Name: {name}\n" \
                               f"Topic: {topic}\n" \
                               f"Email: {email}\n" \
                               f"Contact Number: {contact_number}\n" \
                               f"Registration Result: {registration_result}"

        messagebox.showinfo("Registration Result", confirmation_message)

    def view_info(self):
        registration_number = self.name_entry.get()

        if registration_number:
            participant_info = self.event_registration.get_participant_info(registration_number)
            if participant_info:
                info = f"Name: {participant_info.name}\n" \
                       f"Topic: {participant_info.topic}\n" \
                       f"Email: {participant_info.email}\n" \
                       f"Contact Number: {participant_info.contact_number}"
                messagebox.showinfo(f"{self.registration_type} Information", info)
            else:
                messagebox.showinfo("Participant Not Found", "Participant with the provided registration number not found.")
        else:
            messagebox.showwarning("Input Error", "Please enter a registration number.")

    def update_info(self):
        registration_number = self.name_entry.get()

        if registration_number:
            name = self.name_entry.get()
            topic = self.topic_entry.get()
            email = self.email_entry.get()
            contact_number = self.contact_entry.get()

            update_method = getattr(self.event_registration, f"update_{self.registration_type.lower()}")
            update_result = update_method(registration_number, name, topic, email, contact_number)

            messagebox.showinfo("Update Result", update_result)
        else:
            messagebox.showwarning("Input Error", "Please enter a registration number.")

    def delete_info(self):
        registration_number = self.name_entry.get()

        if registration_number:
            delete_method = getattr(self.event_registration, f"delete_{self.registration_type.lower()}")
            delete_result = delete_method(registration_number)

            messagebox.showinfo("Deletion Result", delete_result)
        else:
            messagebox.showwarning("Input Error", "Please enter a registration number.")

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.current_user = None

        self.role_selection_gui = RoleSelectionGUI(master, self.on_role_selection)

    def on_role_selection(self, selected_role):
        self.master.title(f"Event Registration System - {selected_role}")
        self.role_selection_gui.label.destroy()
        self.role_selection_gui.continue_button.destroy()

        self.current_user = User("", "", selected_role)

        credential_entry_gui = CredentialEntryGUI(self.master, selected_role, self.on_credentials_entry)

    def on_credentials_entry(self, username, password):
        if username and password:
            messagebox.showinfo("Authentication Successful", f"Welcome, {self.current_user.role}!")
            self.show_registration_gui()
        else:
            messagebox.showerror("Authentication Failed", "Invalid credentials. Please try again.")

    def show_registration_gui(self):
        notebook = ttk.Notebook(self.master)
        notebook.pack(fill=tk.BOTH, expand=True)

        participant_tab = tk.Frame(notebook)
        organizer_tab = tk.Frame(notebook)

        notebook.add(participant_tab, text="Participant Registration")
        notebook.add(organizer_tab, text="Organizer Operations")

        participant_registration_gui = EventRegistrationGUI(participant_tab, "Participant", "Participant", self.current_user)
        exhibitor_registration_gui = EventRegistrationGUI(organizer_tab, "Exhibitor", "Exhibitor", self.current_user)
        speaker_registration_gui = EventRegistrationGUI(organizer_tab, "Speaker", "Speaker", self.current_user)
        observer_registration_gui = EventRegistrationGUI(organizer_tab, "Observer", "Observer", self.current_user)

        self.event_registration = EventRegistration()

if __name__ == "__main__":
    root = tk.Tk()
    main_app = MainApplication(root)
    root.mainloop()
