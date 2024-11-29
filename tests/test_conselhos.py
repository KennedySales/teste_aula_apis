# test_conselhos.py
import requests
import pytest

BASE_URL = "https://api.adviceslip.com/advice"

def test_get_random_advice_success():
    """Teste de sucesso: Verifica se a requisição retorna status code 200."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Status code deve ser 200"
    
    data = response.json()
    assert "slip" in data, "A chave 'slip' deve estar presente na resposta"
    assert "advice" in data["slip"], "A chave 'advice' deve estar presente dentro de 'slip'"
    assert isinstance(data["slip"]["advice"], str), "O valor da chave 'advice' deve ser uma string"

def test_get_random_advice_content():
    """Verifica se o conselho retornado contém informações válidas."""
    response = requests.get(BASE_URL)
    data = response.json()
    
    assert "slip" in data, "A chave 'slip' deve estar presente na resposta"
    assert "advice" in data["slip"], "A chave 'advice' deve estar presente dentro de 'slip'"
    assert len(data["slip"]["advice"]) > 0, "O conselho deve ter comprimento maior que 0"

def test_get_random_advice_multiple_times():
    """Verifica se múltiplas requisições retornam conselhos diferentes."""
    advice_set = set()
    for _ in range(10):
        response = requests.get(BASE_URL)
        data = response.json()
        advice_set.add(data["slip"]["advice"])
    
    assert len(advice_set) > 1, "Deve haver mais de um conselho diferente retornado"

def test_get_random_advice_invalid_url():
    """Teste de erro: Verifica o comportamento com URL inválida."""
    response = requests.get("https://api.adviceslip.com/invalid")
    assert response.status_code == 404, "Status code deve ser 404 para URL inválida"

def test_get_random_advice_no_content():
    """Verifica se não há conteúdo ao fazer uma requisição vazia."""
    response = requests.get(BASE_URL + "?amount=0")
    assert response.status_code == 200, "Status code deve ser 200"
    data = response.json()
    assert "slip" in data, "A chave 'slip' deve estar presente na resposta"
    assert data["slip"]["advice"] == "", "O conselho deve ser uma string vazia quando a quantidade é 0"
