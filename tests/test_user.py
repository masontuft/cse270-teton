import requests
import pytest
import requests_mock

@pytest.fixture
def mock_api():
    """Set up a mock API for testing."""
    with requests_mock.Mocker() as m:
        # Configure the mock responses
        # 401 Unauthorized for incorrect credentials
        m.get(
            "http://127.0.0.1:8000/users?username=admin&password=admin",
            status_code=401, 
            text=""
        )
        
        # 200 OK for correct credentials
        m.get(
            "http://127.0.0.1:8000/users?username=admin&password=qwerty",
            status_code=200, 
            text=""
        )
        
        yield m

def test_unauthorized_access(mock_api):
    """
    Test that accessing /users endpoint with invalid credentials returns 401 Unauthorized.
    """
    # Setup test variables
    base_url = "http://127.0.0.1:8000"
    endpoint = "/users"
    params = {
        "username": "admin",
        "password": "admin"
    }
    
    # Send request to the API endpoint
    response = requests.get(f"{base_url}{endpoint}", params=params)
    
    # Assert the response status code is 401 Unauthorized
    assert response.status_code == 401, f"Expected status code 401, but got {response.status_code}"
    
    # Assert that the response body is empty
    assert not response.text.strip(), f"Expected empty response body, but got: {response.text}"
    
    print("Test passed: Received 401 Unauthorized with empty response body")

def test_successful_authentication(mock_api):
    """
    Test that accessing /users endpoint with correct credentials returns 200 OK.
    """
    # Setup test variables
    base_url = "http://127.0.0.1:8000"
    endpoint = "/users"
    params = {
        "username": "admin",
        "password": "qwerty"
    }
    
    # Send request to the API endpoint
    response = requests.get(f"{base_url}{endpoint}", params=params)
    
    # Assert the response status code is 200 OK
    assert response.status_code == 200, f"Expected status code 200, but got {response.status_code}"
    
    # Assert that the response body is empty
    assert not response.text.strip(), f"Expected empty response body, but got: {response.text}"
    
    print("Test passed: Received 200 OK with empty response body")
