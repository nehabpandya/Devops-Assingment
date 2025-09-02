import pytest
from app import app


@pytest.fixture
def client():
    app.testing = True
    return app.test_client()


def test_home(client):
    res = client.get("/")
    assert res.status_code == 200
    assert "Welcome" in res.get_json()["message"]


def test_health(client):
    res = client.get("/health")
    assert res.status_code == 200
    assert res.get_json()["status"] == "ok"


def test_add_and_get_workouts(client):
    # Add workout
    res = client.post("/workouts", json={"workout": "Pushups", "duration": 30})
    assert res.status_code == 201
    data = res.get_json()
    assert data["workout"]["workout"] == "Pushups"

    # Get workouts
    res = client.get("/workouts")
    assert res.status_code == 200
    workouts = res.get_json()["workouts"]
    assert len(workouts) >= 1
