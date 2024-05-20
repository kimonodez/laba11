from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_version():
    response = client.get("/version/")
    assert response.status_code == 200
    assert response.json() == {"version": "1.0.0"}

def test_get_posts():
    response = client.get("/posts/")
    assert response.status_code == 200
    assert len(response.json()) == 2

def test_create_post():
    new_post = {"id": 3, "title": "Third Post", "content": "This is the third post."}
    response = client.post("/posts/", json=new_post)
    assert response.status_code == 200
    assert response.json() == new_post

def test_update_post():
    updated_post = {"id": 1, "title": "Updated First Post", "content": "This is the updated first post."}
    response = client.put("/posts/1", json=updated_post)
    assert response.status_code == 200
    assert response.json() == updated_post

def test_delete_post():
    response = client.delete("/posts/1")
    assert response.status_code == 200
    assert response.json() == {"id": 1, "title": "First Post", "content": "This is the first post."}
    
    response = client.get("/posts/")
    assert len(response.json()) == 2  # One post is deleted, so two should remain

def test_stats():
    response = client.get("/stats/")
    assert response.status_code == 200
    assert "version" in response.json()
    assert "posts" in response.json()
