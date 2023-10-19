import pytest
import requests
import json

@pytest.fixture(scope='session')
def request_session():
    session = requests.session()
    yield session
    session.close()

@pytest.fixture(scope='session')
def preload_requests(request_session):
    headers = {
        "content-type": "application/json"
    }
    for i in range(1,10):
        body = {
            "id": i,
            "petId": 0,
            "quantity": 0,
            "shipDate": "2023-10-17T17:41:50.782Z",
            "status": "placed",
            "complete": True
        }
        request_session.post('https://petstore.swagger.io/v2/store/order/', headers=headers, data=json.dumps(body))