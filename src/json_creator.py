import random
import string
import datetime
import enum


class EventTypes(enum.Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class EventPlaces(enum.Enum):
    ZOOM = "zoom"
    TELEGRAM = "telegram"
    SKYPE = "skype"
    DISCORD = "discord"
    OTHER = "other"


class DictEventsCreator:
    DEFAULT_START_DATE = datetime.datetime(year=2015, month=5, day=12, hour=15,
                                           minute=22, second=24, tzinfo=datetime.timezone.utc)
    DEFAULT_END_DATE = datetime.datetime(year=2023, month=10, day=20, hour=12,
                                         minute=24, second=44, tzinfo=datetime.timezone.utc)

    def __init__(self, event_date='2019-07-07 01:04:00+00:00', event_type='meeting', title='About programms', members=['Vladimir', 'Alexander'], place='zoom'):
        self.event_date = event_date
        self.event_type = place
        self.title = title
        self.members = members
        self.place = place

    def create_datetime(self, start_date=DEFAULT_START_DATE, end_date=DEFAULT_END_DATE):
        delta = end_date - start_date
        seconds_delta = delta.total_seconds()
        random_second = random.randint(0, int(seconds_delta))
        random_date_time = start_date + \
            datetime.timedelta(seconds=random_second)
        return datetime.datetime.strftime(random_date_time, '%Y-%m-%d %H:%M:%S%z')

    def create_event_type(self):
        return random.choice(list(EventTypes)).value

    def create_title(self):
        words = ['users', 'programms', 'weather', 'events',
                 'books', 'space', 'cars', 'houses', 'test']
        self.title = 'About ' + random.choice(words)
        return self.title

    def add_users(self):
        users = ['Vladimir', 'Ivan', 'Artem', 'Roman', 'Vasiliy', 'Alexandr']
        self.members = random.sample(users, 5)

        return self.members

    def create_place(self):
        self.place = random.choice(list(EventPlaces)).value
        return self.place

    def get_event(self):
        return {
            'datetime': self.create_datetime(),
            'event_type': self.create_event_type(),
            'title': self.create_title(),
            'members': self.add_users(),
            'place': self.create_place()
        }
