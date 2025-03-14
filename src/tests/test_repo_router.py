import pytest
from fastapi.testclient import TestClient
import os

def test_create_repo_success(client: TestClient):
    """Test successful repository cloning."""
    response = client.post(
        "/api/v1/repos",
        json={
            "url": "https://github.com/karawalla/code-architect",
            "branch": "V1"
        }
    )
    
    assert response.status_code == 200
    data = response.json()
    assert "local_path" in data
    assert data["repo_name"] == "code-architect"
    assert data["branch"] == "V1"
    assert os.path.exists(data["local_path"])

def test_create_repo_invalid_url(client: TestClient):
    """Test error handling for invalid repository URL."""
    response = client.post(
        "/api/v1/repos",
        json={
            "url": "https://github.com/invalid/repo",
            "branch": "main"
        }
    )
    
    assert response.status_code == 400
    assert "Failed to clone repository" in response.json()["detail"]

def test_create_repo_invalid_branch(client: TestClient):
    """Test error handling for invalid branch name."""
    response = client.post(
        "/api/v1/repos",
        json={
            "url": "https://github.com/karawalla/code-architect",
            "branch": "nonexistent-branch"
        }
    )
    
    assert response.status_code == 400
    assert "Failed to clone repository" in response.json()["detail"]
