import pytest
from flask_app import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_route(client):
    response = client.get('/')
    assert response.status_code == 200
    assert b'Camiseta' in response.data

def test_agregar_producto(client):
    response = client.post('/agregar/1')
    assert response.status_code == 200
    data = response.get_json()
    assert data["mensaje"] == "Producto agregado"
    assert len(data["carrito"]) > 0

def test_carrito_total(client):
    client.post('/agregar/2')
    response = client.get('/carrito')
    data = response.get_json()
    assert "total" in data
    assert data["total"] >= 0
