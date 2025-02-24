from fastapi.testclient import TestClient
import sys
import os
import pytest

sys.path.append(os.path.dirname(os.path.dirname(__file__)))  # Adds project root to Python path

from app.main import app  # Adjust import if 'main.py' is at the root level


client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to the Trade Orders API!"}
