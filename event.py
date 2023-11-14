
class Event:
    def __init__(self,name, date, description):
        self._name = name
        self._date = date
        self._description = description
        self._speakers = []
        self._exhibitors = []
        self._observers = []

    # Getter and Setter for the 'name' attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for the 'date' attribute
    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    # Getter and Setter for the 'description' attribute
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def register_speaker(self, speaker_name):
        self._speakers.append(speaker_name)

    def register_exhibitor(self, exhibitor_name):
        self._exhibitors.append(exhibitor_name)

    def register_observer(self, observer_name):
        self._observers.append(observer_name)

    def get_event_details(self):
        return f"Event: {self._name}\nDate: {self._date}\nDescription: {self._description}"

    def get_speakers(self):
        return f"Speakers: {', '.join(self._speakers)}"

    def get_exhibitors(self):
        return f"Exhibitors: {', '.join(self._exhibitors)}"

    def get_observers(self):
        return f"Observers: {', '.join(self._observers)}"

'''



events = []
def create_event():
    event_name = input("Enter event name: ")
    event_date = input("Enter event date: ")
    event_description = input("Enter event description: ")

    event = {
        'name': event_name,
        'date': event_date,
        'description': event_description
    }

    events.append(event)

def add_event():
    event_name = input("Enter event name: ")
    event_date = input("Enter event date: ")
    event_description = input("Enter event description: ")

    event = {
        'name': event_name,
        'date': event_date,
        'description': event_description
    }

    events.append(event)

def modify_event():
    event_index = int(input("Enter the index of the event you want to modify: ")) - 1
    if 0 <= event_index < len(events):
        event = events[event_index]
        print(f"Current event data: {event}")
        event_name = input("Enter new event name (press Enter to keep current): ")
        event_date = input("Enter new event date (press Enter to keep current): ")
        event_description = input("Enter new event description (press Enter to keep current): ")

        if event_name:
            event['name'] = event_name
        if event_date:
            event['date'] = event_date
        if event_description:
            event['description'] = event_description

        events[event_index] = event
        print("Event modified successfully.")
    else:
        print("Invalid event index.")

def delete_event():
    event_index = int(input("Enter the index of the event you want to delete: ")) - 1
    if 0 <= event_index < len(events):
        del events[event_index]
        print("Event deleted successfully.")
    else:
        print("Invalid event index.")

        '''