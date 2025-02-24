from fastapi.testclient import TestClient
from app.main import app  # Adjust the import if your structure differs

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the API!"}
