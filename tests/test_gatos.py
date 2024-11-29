# test_gatos.py
import requests
import pytest

BASE_URL = "https://catfact.ninja/fact"

def test_get_random_fact_success():
    """Teste de sucesso: Verifica se a requisição retorna status code 200."""
    response = requests.get(BASE_URL)
    assert response.status_code == 200, "Status code deve ser 200"
    
    data = response.json()
    assert "fact" in data, "A chave 'fact' deve estar presente na resposta"
    assert isinstance(data["fact"], str), "O valor da chave 'fact' deve ser uma string"

def test_get_random_fact_content():
    """Verifica se o fato retornado contém informações válidas."""
    response = requests.get(BASE_URL)
    data = response.json()
    
    assert "fact" in data, "A chave 'fact' deve estar presente na resposta"
    assert len(data["fact"]) > 0, "O fato deve ter comprimento maior que 0"

def test_get_random_fact_multiple_times():
    """Verifica se múltiplas requisições retornam fatos diferentes."""
    facts = set()
    for _ in range(10):
        response = requests.get(BASE_URL)
        data = response.json()
        facts.add(data["fact"])
    
    assert len(facts) > 1, "Deve haver mais de um fato diferente retornando"

def test_get_random_fact_invalid_url():
    """Teste de erro: Verifica o comportamento com URL inválido."""
    response = requests.get("https://catfact.ninja/invalid")
    assert response.status_code == 404, "Status code deve ser 404 para URL inválida"

def test_get_random_fact_no_content():
    """Verifica se não há conteúdo ao fazer uma requisição vazia."""
    response = requests.get(BASE_URL + "?amount=0")
    assert response.status_code == 200, "Status code deve ser 200"
    data = response.json()
    assert "fact" in data, "A chave 'fact' deve estar presente na resposta"
    assert data["fact"] == "", "O fato deve ser uma string vazia quando a quantidade é 0"
