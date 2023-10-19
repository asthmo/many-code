import pytest
import random
import json

from datetime import datetime
from src.Event import EventEditor
from src.json_creator import json_Creator
# r

@pytest.fixture(scope='module')
def event_object():
    event = EventEditor()
    events_list = event.load_data_from_file('./src/events.json')
    return event

def test_read_file(event_object):
    list_check_fields = [True if list(event.keys()) == ['datetime', 'event_type', 'title', 'members', 'place'] else False for event in event_object.get_events()]
    assert list_check_fields.count(True) == len(event_object.get_events())

def test_sort_events_list(event_object):
    sorted_events = list(event_object.sort_and_form().keys())
    
    # указываю 1, потому что при переборе и сравнении дат, мы не проверяем последнюю дату
    true_counter = 1

    for event_date_i in range(0, len(sorted_events)-1):
        if datetime.strptime(sorted_events[event_date_i], '%Y-%m-%d') < datetime.strptime(sorted_events[event_date_i+1], '%Y-%m-%d'):
            true_counter += 1
    
    assert true_counter == len(sorted_events)

def test_write_events(event_object, event_create):
    data = []
    for _ in range(2,random.randint(3,10)):
        data.append(event_create.get_event())
    sort_data = event_object.sort_and_form(data)
    event_object.create_json_file('test_json.json', sort_data)

    with open('test_json.json','r') as f:
        json_str = json.loads(f.read())
        
    assert json_str == sort_data