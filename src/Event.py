from datetime import datetime
import time
import json
import argparse

class Event:
    AVAILABLE_EVENT_TYPES = ("private", "meeting", "corporate", "other")

    def __init__(self, date_time: str, event_type: str, title: str, members: list[str], place:str):
        self.date_time = date_time
        self.event_type = event_type
        self.title = title
        if self.__check_event_type(self.event_type):
            self.event_type = event_type
        self.members = members
        self.place = place

    @classmethod
    def __check_event_type(cls, event_type):
        if event_type in cls.AVAILABLE_EVENT_TYPES:
            return True
        else:
            raise ValueError('Event type not available!')

    def get_datetime(self):
        return self.date_time
        
    def str_to_date(self):
        my_date = datetime.strptime(self.date_time.split(' ')[0], '%Y-%m-%d')

        return my_date

class EventEditor:
    def load_data_from_file(self,file_name):
        with open(file_name, 'r') as f:
            self.event_list = json.loads(f.read())

    def get_events(self):
        return self.event_list
        
    def sort_and_form(self, events = []):
        events_for_sort = []
        if len(events) == 0:
            events_for_sort = self.event_list
        else:
            events_for_sort = events
        result = {}
        out = {}
        events_for_sort = sorted(events_for_sort, key = lambda x: datetime.strptime(x['datetime'].split()[0], '%Y-%m-%d'), reverse=False)

        for event in events_for_sort:
            event_info = Event(event['datetime'], event['event_type'], event['title'], event['members'], event['place'])
            date = event_info.get_datetime().split()[0]

            if date in result:
                result[date].append(event)
            else:
                result[date] = [event]

        for key,value in result.items():
            value = sorted(value, key= lambda x: datetime.strptime(x['datetime'], '%Y-%m-%d %H:%M%z'))
            
            if key in out:
                out[value].append(value)
            else:
                out[key] = value
        return out
    

    def create_json_file(self, file_name, output):
        with open(file_name, 'w') as file:
            json.dump(output, file, indent=3)


if __name__ == '__main__':
    start_script = argparse.ArgumentParser(description='Sort json file with events')
    start_script.add_argument('input_file', type=str, help='Input file')
    start_script.add_argument('output_file', type=str, help='Output file')
    args = start_script.parse_args()


    forming_data = EventEditor()
    forming_data.load_data_from_file(args.input_file)
    ready_data = forming_data.sort_and_form()
    forming_data.create_json_file(args.output_file, ready_data)