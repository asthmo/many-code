import pytest
from src.json_creator import json_Creator

@pytest.fixture
def event_create():
    event = json_Creator()
    return event