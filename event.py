
class Event:
    def init (self,name,date,desc):
        self.name
        self.date
        self.desc

    


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