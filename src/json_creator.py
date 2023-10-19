import random
import string
from datetime import datetime, timedelta, timezone

class json_Creator:
    AVAILABLE_EVENT_TYPES = ("private", "meeting", "corporate", "other")


    def __init__(self, date_time = '', event_type = '', title = '', members = [], place = '', time_delta = ''):
        self.date_time = date_time
        self.event_type = event_type
        self.title = title
        self.members = members
        self.place = place

    def create_datetime(self):
        min_year = 2000
        max_year=datetime.now().year
        start = datetime(year=min_year, month=1, day=1, hour=00, minute=00, tzinfo=timezone.utc)
        years = max_year - min_year + 1
        end = start + timedelta(days=365 * years)
        self.date_time = datetime.strftime(start + (end - start) * random.random(), '%Y-%m-%d %H:%M%z')
        return self.date_time

    def create_event_type(self):
        return random.choice(self.AVAILABLE_EVENT_TYPES)
    
    def create_title(self):
        words = ['users', 'programms', 'weather', 'events', 'books', 'space', 'cars', 'houses', 'test']
        self.title = 'About ' + random.choice(words)
        return self.title
    
    def add_users(self):
        users = ['Vladimir', 'Ivan', 'Artem', 'Roman', 'Vasiliy', 'Alexandr']
        for _ in range(1,random.randint(2,5)):
            self.members.append(random.choice(users))

        return self.members
    
    def create_place(self):
        places = ['zoom', 'telegram', 'skype', 'discord', 'other']
        self.place = random.choice(places)
        return self.place
    
    def get_event(self):
        return {
            'datetime' : self.create_datetime(),
            'event_type' : self.create_event_type(),
            'title' : self.create_title(),
            'members' : self.add_users(),
            'place' : self.create_place()
        }