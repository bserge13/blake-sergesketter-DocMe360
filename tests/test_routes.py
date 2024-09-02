import pytest 
from flask import json

# Template routes
def test_get_template(client):
    response = client.post("/api/template", json = {"body": "Test Template"})
    template_id = response.get_json()["id"]

    response = client.get(f"/api/template/{template_id}")
    data = response.get_json()

    assert response.status_code == 200
    assert "id" in data 
    assert data["id"] == template_id
    assert "body" in data 
    assert data["body"] == "Test Template"

def test_get_templates(client):
    response = client.get("/api/template")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) != 0 
    # test dependant on the current state of the database (currently has Templates in db)

def test_post_template(client):
    response = client.post("/api/template", json = {
        "body": "Hello, (peronsal). How are you today, (personal)?"
        })
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["body"] == "Hello, (peronsal). How are you today, (personal)?"

def test_patch_template(client):
    response = client.post("/api/template", json = {"body": "Original Test Template"})
    template_id = response.get_json()["id"]

    response = client.patch(f"/api/template/{template_id}", json = {
        "body": "Updated Test Template"
    })
    updated_temp = client.get(f"/api/template/{template_id}")
    data = updated_temp.get_json()

    assert response.status_code == 200
    assert data["body"] == "Updated Test Template"

def test_delete_template (client):
    response = client.post("/api/template", json = {"body": "Delete Template"})
    template_id = response.get_json()["id"]

    response = client.delete(f"/api/template/{template_id}")
    deleted = client.get(f"/api/template/{template_id}")

    assert response.status_code == 200
    assert deleted.status_code == 404



# Notification routes
def test_get_notification(client):
    template = client.post("/api/template", json = {"body": "Test Template"})
    template_id = template.get_json()["id"]
    notification = client.post("/api/notification", json = {
        "phone_number": "Test Number", 
        "personalization": "Test Name",
        "template_id": template_id
    })
    notification_id = notification.get_json()["id"]

    response = client.get(f"/api/notification/{notification_id}")
    data = response.get_json()

    assert response.status_code == 200
    assert "id" in data 
    assert data["id"] == notification_id
    assert "phone_number" in data 
    assert data["phone_number"] == "Test Number"
    assert "personalization" in data 
    assert data["personalization"] == "Test Name"
    assert "template_id" in data 
    assert data["template_id"] == template_id
    assert "content" in data 
    assert data["content"] == "Test Template"

def test_get_notifications(client):
    response = client.get("/api/notification")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) != 0 

def test_post_notification(client):
    response = client.post("/api/notification", json = {
            "phone_number": "671-992-8979",
            "personalization": "John-Paul",
            "template_id": 1
        })
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["phone_number"] == "671-992-8979"
    assert data["personalization"] == "John-Paul"
    assert data["template_id"] == 1

def test_delete_notification (client):
    template = client.post("/api/template", json = {"body": "Deletable Template"})
    template_id = template.get_json()["id"]
    
    notification = client.post("/api/notification", json = {
        "phone_number": "Test Number", 
        "personalization": "Test Name",
        "template_id": template_id
    })
    notification_id = notification.get_json()["id"]

    response = client.delete(f"/api/template/{notification_id}")
    deleted = client.get(f"/api/template/{notification_id}")

    assert response.status_code == 200
    assert deleted.status_code == 404
