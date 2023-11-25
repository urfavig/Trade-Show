import tkinter as tk
from tkinter import messagebox

class ParticipantsReportGUI:
    def __init__(self, master, event_registration):
        self.master = master
        self.event_registration = event_registration

        # Button to generate a report on the number of participants
        generate_report_button = tk.Button(master, text="Generate Participants Report", command=self.generate_participants_report)
        generate_report_button.pack(pady=10)

    def generate_participants_report(self):
        # Count the number of participants for each type
        exhibitor_count = len(self.event_registration.exhibitors)
        speaker_count = len(self.event_registration.speakers)
        observer_count = len(self.event_registration.observers)

        # Display the report in a message box
        report_message = f"Participants Report:\n\nExhibitors: {exhibitor_count}\nSpeakers: {speaker_count}\nObservers: {observer_count}"
        messagebox.showinfo("Participants Report", report_message)

if __name__ == "__main__":
    root = tk.Tk()
    event_registration = EventRegistration()  
    participants_report_gui = ParticipantsReportGUI(root, event_registration)
    root.mainloop()
