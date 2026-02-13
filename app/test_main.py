# test_main.py
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World2"}

def test_read_item():
    response = client.get("/items/1")
    assert response.status_code == 200
    assert response.json() == {"item_id": 1, "name": "Item 1"}
    
def test_read_item_invalid_id():
    # Test an invalid input to ensure proper error handling
    response = client.get("/items/abc") 
    assert response.status_code == 422 # 422 Unprocessable Entity for validation errors
