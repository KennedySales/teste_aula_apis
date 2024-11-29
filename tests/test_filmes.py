import pytest
import requests

# URL base da API do TMDB
BASE_URL = "('https://api.themoviedb.org/3')"
API_KEY = "SUA_API_KEY_AQUI"  # adcionar chave API key

def test_get_filme_sucesso():
    """
    Testa se a API retorna informações de um filme específico.
    """
    filme_id = 550  # ID do filme "Toy Story"
    resposta = requests.get(f"{BASE_URL}/movie/{filme_id}", params={"api_key": API_KEY})
    assert resposta.status_code == 200
    assert "title" in resposta.json()

def test_get_filme_id_inexistente():
    """
    Testa se a API retorna erro para ID inexistente.
    """
    filme_id = 999999  # ID inexistente
    resposta = requests.get(f"{BASE_URL}/movie/{filme_id}", params={"api_key": API_KEY})
    assert resposta.status_code == 404

def test_get_filme_sem_api_key():
    """
    Testa se a API retorna erro sem API key.
    """
    filme_id = 550  # ID do filme "Toy Story"
    resposta = requests.get(f"{BASE_URL}/movie/{filme_id}")
    assert resposta.status_code == 401

def test_get_filme_com_parametros_invalidos():
    """
    Testa se a API retorna erro com parâmetros inválidos.
    """
    filme_id = 550  # ID do filme "Toy Story"
    resposta = requests.get(f"{BASE_URL}/movie/{filme_id}", params={"api_key": API_KEY, "invalido": "123"})
    assert resposta.status_code == 400

def test_get_filme_com_dados_esperados():
    """
    Testa se a API retorna dados esperados.
    """
    filme_id = 550  # ID do filme "Toy Story"
    resposta = requests.get(f"{BASE_URL}/movie/{filme_id}", params={"api_key": API_KEY})
    dados = resposta.json()
    assert dados["title"] == "Toy Story"
    assert dados["original_language"] == "en"