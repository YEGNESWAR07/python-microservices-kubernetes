import pytest
from app import app

def test_root():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200
    assert "message" in response.get_json()
