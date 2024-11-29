import pytest
import requests

# URL base da API da Starlink
BASE_URL = "(link unavailable)"

def test_get_starlink_satellites():
    """
    Testa se a API retorna uma lista de satélites Starlink.
    """
    resposta = requests.get(BASE_URL)
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), list)

def test_get_starlink_satellite_id():
    """
    Testa se a API retorna informações de um satélite específico.
    """
    satellite_id = "5eedf5ecb9424f6b83880938"  # ID de exemplo
    resposta = requests.get(f"{BASE_URL}/{satellite_id}")
    assert resposta.status_code == 200
    assert isinstance(resposta.json(), dict)

def test_get_starlink_satellite_id_inexistente():
    """
    Testa se a API retorna erro para ID inexistente.
    """
    satellite_id = "1234567890"  # ID inexistente
    resposta = requests.get(f"{BASE_URL}/{satellite_id}")
    assert resposta.status_code == 404

def test_post_starlink_satellite():
    """
    Testa se a API não permite criar novos satélites via POST.
    """
    resposta = requests.post(BASE_URL, json={})
    assert resposta.status_code == 405

def test_put_starlink_satellite():
    """
    Testa se a API não permite atualizar satélites via PUT.
    """
    satellite_id = "5eedf5ecb9424f6b83880938"  # ID de exemplo
    resposta = requests.put(f"{BASE_URL}/{satellite_id}", json={})
    assert resposta.status_code == 405

def test_delete_starlink_satellite():
    """
    Testa se a API não permite excluir satélites via DELETE.
    """
    satellite_id = "5eedf5ecb9424f6b83880938"  # ID de exemplo
    resposta = requests.delete(f"{BASE_URL}/{satellite_id}")
    assert resposta.status_code == 405

def test_get_starlink_satellite_params_invalidos():
    """
    Testa se a API retorna erro para parâmetros inválidos.
    """
    resposta = requests.get(f"{BASE_URL}?parametro_invalido=123")
    assert resposta.status_code == 400

def test_get_starlink_satellite_conexao_errada():
    """
    Testa se a API retorna erro para conexão errada.
    """
    BASE_URL_ERRADA = "(link unavailable)"
    resposta = requests.get(BASE_URL_ERRADA)
    assert resposta.status_code == 404

def test_get_starlink_satellite_timeout():
    """
    Testa se a API retorna erro para timeout.
    """
    resposta = requests.get(BASE_URL, timeout=0.001)
    assert resposta.status_code == 408

def test_get_starlink_satellite_json_invalido():
    """
    Testa se a API retorna erro para JSON inválido.
    """
    resposta = requests.get(BASE_URL, headers={"Content-Type": "application/json"}, data="json_invalido")
    assert resposta.status_code == 400