import pytest
from main import app


@pytest.fixture
def client():
    """Create a test client for the Flask app."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client


def test_hello_world_status_code(client):
    """Test that the root endpoint returns 200 status code."""
    response = client.get('/')
    assert response.status_code == 200


def test_hello_world_content(client):
    """Test that the root endpoint returns correct content."""
    response = client.get('/')
    assert response.data == b'Hello World!'


def test_hello_world_content_type(client):
    """Test that the response has correct content type."""
    response = client.get('/')
    assert response.content_type == 'text/html; charset=utf-8'


def test_nonexistent_route(client):
    """Test that non-existent routes return 404."""
    response = client.get('/nonexistent')
    assert response.status_code == 404


def test_hello_world_wrong_content(client):
    """This test will fail - expecting wrong content."""
    response = client.get('/')
    assert response.data == b'Goodbye World!'
