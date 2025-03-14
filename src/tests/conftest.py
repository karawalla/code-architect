import pytest
from fastapi.testclient import TestClient
import os
import shutil
from main import app

@pytest.fixture
def client():
    return TestClient(app)

@pytest.fixture(autouse=True)
def clean_test_repos():
    # Setup: Create test repos directory
    test_repos_path = "./test_repos"
    os.environ["REPOS_PATH"] = test_repos_path
    os.makedirs(test_repos_path, exist_ok=True)
    
    yield
    
    # Teardown: Clean up test repos
    shutil.rmtree(test_repos_path, ignore_errors=True)
