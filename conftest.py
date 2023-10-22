import pytest
from src.json_creator import DictEventsCreator


@pytest.fixture
def event_create():
    event = DictEventsCreator()
    return event
