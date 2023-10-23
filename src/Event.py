from datetime import datetime
import time
import json
import argparse
import enum


class EventTypes(enum.Enum):
    PRIVATE = "private"
    MEETING = "meeting"
    CORPORATE = "corporate"
    OTHER = "other"


class Event:
    def __init__(self, event_date: str, event_type: str, title: str, members: list[str], place: str):
        self.event_date = event_date
        self.event_type = event_type
        self.title = title
        self.event_type = EventTypes(event_type)
        self.members = members
        self.place = place

    @classmethod
    def from_dict(cls, event_dict: dict):
        return cls(event_dict['datetime'], event_dict['title'], event_dict['event_type'], event_dict['members'], event_dict['place'])

    def get_datetime(self):
        return self.event_date

    def str_to_date(self):
        my_date = datetime.strptime(self.event_date.split(' ')[0], '%Y-%m-%d')
        return my_date


class EventHandler:
    def load_data_from_file(self, file_name):
        with open(file_name, 'r', encoding='utf-8') as f:
            self.event_list = json.loads(f.read())
        return self.event_list

    def get_events(self):
        return self.event_list

    def sort_and_form(self):
        result = {}
        event_list = sorted(self.event_list, key=lambda x: datetime.strptime(
            x['datetime'].split()[0], '%Y-%m-%d'), reverse=False)
        
        for event in event_list:
            event_info = Event(event['datetime'], event['event_type'],
                               event['title'], event['members'], event['place'])
            date = event_info.get_datetime().split()[0]
            if date in result:
                result[date].append(event)
                result[date] = sorted(result[date], key=lambda x: datetime.strptime(
                    x['datetime'], '%Y-%m-%d %H:%M%z'))
            else:
                result[date] = [event]
                
        return result

    def create_json_file(self, file_name, output):
        with open(file_name, 'w') as file:
            json.dump(output, file, indent=3)

