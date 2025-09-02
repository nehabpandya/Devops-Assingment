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
    
def test_delete_workout(client):
    """Test deleting an existing workout and handling an invalid index."""
    # First, add a workout to be able to delete it
    client.post("/workouts", json={"workout": "Crunches", "duration": 15})
    client.post("/workouts", json={"workout": "Running", "duration": 45})

    # Test successful deletion of the first workout
    res = client.delete("/workouts/0")
    assert res.status_code == 200
    assert res.get_json()["message"] == "'Crunches' workout deleted successfully!"

    # Check if the workout list has been updated
    res = client.get("/workouts")
    assert len(res.get_json()["workouts"]) == 1
    assert res.get_json()["workouts"][0]["workout"] == "Running"

    # Test deleting with an invalid index
    res = client.delete("/workouts/999")
    assert res.status_code == 404
    assert res.get_json()["error"] == "Workout not found"

    # Test deleting from an empty list
    client.delete("/workouts/0")  # Delete the last remaining workout
    res = client.delete("/workouts/0") # Attempt to delete from empty list
    assert res.status_code == 404
    assert res.get_json()["error"] == "Workout not found"