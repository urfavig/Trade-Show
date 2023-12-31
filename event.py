#event.py
class Event:
    def __init__(self,name, start_date,end_date, description, booth_amount):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._description = description
        self._speakers = []
        self._exhibitors = []
        self._observers = []
        self._booth_amount = booth_amount
        self._booths = []

    # Getter and Setter for the 'name' attribute
    def get_name(self):
        return self._name

    def set_name(self, name):
        self._name = name

    # Getter and Setter for the 'date' attribute
    def get_start_date(self):
        return self._start_date

    def set_start_date(self, date):
        self._start_date = date

    # Getter and Setter for the 'date' attribute
    def get_end_date(self):
        return self._end_date

    def set_end_date(self, date):
        self._end_date = date

    # Getter and Setter for the 'description' attribute
    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def get_booth_amount(self):
        return self._booth_amount

    def set_booth_amount(self, booth_amount):
        self._booth_amount = booth_amount

    def register_speaker(self, speaker_name):
        self._speakers.append(speaker_name)

    def register_exhibitor(self, exhibitor_name):
        self._exhibitors.append(exhibitor_name)

    def register_observer(self, observer_name):
        self._observers.append(observer_name)

    def get_event_details(self):
        return f"Event: {self._name}\nStart Date: {self._start_date}\nEnd Date: {self._end_date}\nDescription: {self._description}"

    def get_speakers(self):
        return f"Speakers: {', '.join(self._speakers)}"

    def get_exhibitors(self):
        return f"Exhibitors: {', '.join(self._exhibitors)}"

    def get_observers(self):
        return f"Observers: {', '.join(self._observers)}"
