class Event:
    def __init__(self,name, start_date,end_date, description,booths):
        self._name = name
        self._start_date = start_date
        self._end_date = end_date
        self._description = description
        self._speakers = []
        self._exhibitors = []
        self._observers = []
        self._booths = []

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
