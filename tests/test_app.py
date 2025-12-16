import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_positive(client):
    """TC-01: Перевірка додавання"""
    response = client.post('/calc', json={'operation': 'add', 'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 15

def test_divide_zero(client):
    """TC-05: Перевірка ділення на нуль"""
    response = client.post('/calc', json={'operation': 'divide', 'a': 10, 'b': 0})
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.get_json()['error']

def test_invalid_input(client):
    """TC-06: Перевірка валідації вхідних даних"""
    response = client.post('/calc', json={'operation': 'add', 'a': 'xyz', 'b': 5})
    assert response.status_code == 400

def test_unknown_operation(client):
    """TC-07: Перевірка невідомої операції"""
    response = client.post('/calc', json={'operation': 'modulus', 'a': 10, 'b': 2})
    assert response.status_code == 400import pytest
from app import app

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_add_positive(client):
    """TC-01: Перевірка додавання"""
    response = client.post('/calc', json={'operation': 'add', 'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.get_json()['result'] == 15

def test_divide_zero(client):
    """TC-05: Перевірка ділення на нуль"""
    response = client.post('/calc', json={'operation': 'divide', 'a': 10, 'b': 0})
    assert response.status_code == 400
    assert "Cannot divide by zero" in response.get_json()['error']

def test_invalid_input(client):
    """TC-06: Перевірка валідації вхідних даних"""
    response = client.post('/calc', json={'operation': 'add', 'a': 'xyz', 'b': 5})
    assert response.status_code == 400

def test_unknown_operation(client):
    """TC-07: Перевірка невідомої операції"""
    response = client.post('/calc', json={'operation': 'modulus', 'a': 10, 'b': 2})
    assert response.status_code == 400
