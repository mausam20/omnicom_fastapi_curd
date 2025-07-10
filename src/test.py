from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

# Sample test data
sample_import = {
    "year": 2005,
    "month": 1,
    "origin_name": "Algeria",
    "origin_type_name": "Country",
    "destination_name": "CHEVRON USA INC / TX",
    "destination_type_name": "Refinery",
    "grade_name": "Light Sweet",
    "quantity": 850.0
}

updated_data = {
    "month": 5
}

bulk_data = {
    "records": [
        {
            "year": 2000,
            "month": 2,
            "origin_name": "Testland",
            "origin_type_name": "Country",
            "destination_name": "TEST CO / TX",
            "destination_type_name": "Refinery",
            "grade_name": "Test Grade",
            "quantity": 100.0
        }
    ]
}

# Test Create Import
def test_create_import():
    response = client.post("/imports/", json=sample_import)
    assert response.status_code == 201
    data = response.json()
    assert data["origin_name"] == "algeria"
    global created_id
    created_id = data["id"]

# Test List Imports with filter
def test_get_imports():
    response = client.get("/imports/?country=algeria&skip=0&limit=10")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

# Test Update Import
def test_update_import():
    response = client.put(f"/imports/?id={created_id}", json=updated_data)
    assert response.status_code == 200
    assert response.json()["month"] == 5

# Test Delete Import
def test_delete_import():
    response = client.delete(f"/imports/?id={created_id}")
    assert response.status_code == 200
    assert response.json()["detail"] == "Deleted"

# Test Bulk Import
def test_bulk_import():
    response = client.post("/imports/bulk", json=bulk_data)
    assert response.status_code == 201
    assert "records inserted successfully" in response.json()["message"]
