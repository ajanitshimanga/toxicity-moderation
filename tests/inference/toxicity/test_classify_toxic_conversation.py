from main import app
from fastapi.testclient import TestClient
import pytest


@pytest.fixture(scope="session", autouse=True)
def client_fixture():
    # setup
    client = TestClient(app)

    yield client

    # clean up


@pytest.mark.asyncio
async def test_toxic_classification(client_fixture):
    conversation_json_payload = {"user_text": "Person 1: Hello how are you doing!\n"
                                 + "Person 2: I am doing great how are you!?\n"}
    response = client_fixture.post("/inference/toxicity/", json=conversation_json_payload)

    assert response.status_code == 200
    assert response is not None
