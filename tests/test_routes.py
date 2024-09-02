import pytest 
from flask import json

# Template routes
def test_get_template(client):
    response = client.get("/api/template/1")
    data = response.get_json()

    assert response.status_code == 200
    assert "id" in data 
    assert data["id"] == 1
    assert "body" in data 
    assert data["body"] == "Hello, (personal), how are you today?"

def test_get_templates(client):
    response = client.get("/api/template")
    data = response.get_json()

    assert response.status_code == 200
    assert len(data) != 0 
    # test dependant on the current state of the database (currently has Templates in db)

def test_post_template(client):
    response = client.post("/api/template", json = {
        "body": "Hello, (peronsal). How are you today, (personal)?",
        })
    data = response.get_json()

    assert response.status_code == 201
    assert "id" in data
    assert data["body"] == "Hello, (peronsal). How are you today, (personal)?"

def test_patch_template(client):
    response = client.patch("/api/template/10", json = {
        "body": "Happy Holiday, (personal)!"
    })
    updated_temp = client.get("/api/template/10")
    data = updated_temp.get_json()

    assert response.status_code == 200
    assert data["body"] == "Happy Holiday, (personal)!"

def test_delete_template (client):
    response = client.delete("/api/template/12")
    deleted = client.get("/api/template/12")

    assert response.status_code == 200
    assert deleted.status_code == 404



# Notification routes
def test_get_notification(client):
    response = client.get("/api/notification/1")
    data = response.get_json()

    assert response.status_code == 200
    assert "id" in data 
    assert data["id"] == 1
    assert "phone_number" in data 
    assert data["phone_number"] == "812-867-5309"
    assert "personalization" in data 
    assert data["personalization"] == "Balakay"
    assert "template_id" in data 
    assert data["template_id"] == 1
    assert "content" in data 
    assert data["content"] == "Hello, Balakay, how are you today?"

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
    response = client.delete("/api/notification/12")
    deleted = client.get("/api/notification/12")

    assert response.status_code == 200
    assert deleted.status_code == 404
