import pytest
import random
import json

from datetime import datetime
from src.event import EventHandler
from src.json_creator import DictEventsCreator
from src.event import EventTypes


@pytest.fixture(scope='module')
def event_handler_object():
    event = EventHandler()
    return event


def test_read_file(event_handler_object):
    events_list = event_handler_object.load_data_from_file('./src/events.json')

    counter_events = 0
    counter_keys = 0
    counter_event_types = 0

    for value in events_list:
        for events in events_list[value]:
            counter_events += 1

            # проверка ключей событий
            if ['datetime', 'event_type', 'title', 'members', 'place'] == list(events.keys()):
                counter_keys += 1

            # Проверка что тип события входит в список допустимых
            if EventTypes(events['event_type']):
                counter_event_types += 1
    
    # Проверка что во всех событиях, переданы все поля
    assert counter_keys == counter_events
    # Проверка что во всех событиях, типы событий являются допустимыми
    assert counter_event_types == counter_events

def test_sort_events_list(event_handler_object):
    events = event_handler_object.load_data_from_file('./src/events.json')
    sorted_events = event_handler_object.sort_and_form(events)
    events_groups_date = all(
        events_group_date < events_group_date+1 for events_group_date in range(len(sorted_events.keys())))

    for key, value in sorted_events.items():
        assert all(
            value[group_i]['datetime'] < value[group_i + 1]['datetime'] for group_i in range(len(value) - 1))

    assert events_groups_date == True


def test_write_events(event_handler_object, event_create):
    data = []
    for _ in range(2, random.randint(3, 10)):
        data.append(event_create.get_event())
    sort_data = event_handler_object.sort_and_form(data)
    event_handler_object.create_json_file('test_json.json', sort_data)

    with open('test_json.json', 'r') as f:
        json_str = json.loads(f.read())

    assert json_str == sort_data
