import pytest
import requests

BASE_URL = "https://pokeapi.co/api/v2/"

def test_get_pokemon_by_name():
    """Testa se podemos obter informações sobre um Pokémon específico pelo nome."""
    response = requests.get(f"{BASE_URL}pokemon/pikachu")
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == 'pikachu'
    assert data['abilities'][0]['ability']['name'] == 'static'

def test_get_pokemon_not_found():
    """Testa se a API retorna um erro 404 para um Pokémon inexistente."""
    # ... (código similar ao exemplo anterior)

# ... outros testes básicos ...

@pytest.mark.parametrize("pokemon, type", [
    ("bulbasaur", "grass"),
    ("charmander", "fire"),
    ("squirtle", "water")
])
def test_pokemon_type(pokemon, type):
    """Testa se o tipo do Pokémon está correto."""
    response = requests.get(f"{BASE_URL}pokemon/{pokemon}")
    assert response.status_code == 200
    data = response.json()
    assert data['types'][0]['type']['name'] == type

@pytest.mark.parametrize("limit, offset", [
    (20, 0),
    (50, 10)
])
def test_pokemon_list(limit, offset):
    """Testa a lista de Pokémons com diferentes limites e offsets."""
    response = requests.get(f"{BASE_URL}pokemon/?limit={limit}&offset={offset}")
    assert response.status_code == 200
    data = response.json()
    assert len(data['results']) == limit

def test_get_pokemon_species():
    """Testa se podemos obter informações sobre a espécie de um Pokémon."""
    # ... (código similar aos outros testes)

def test_get_pokemon_evolution_chain():
    """Testa se podemos obter a cadeia evolutiva de um Pokémon."""
    # ... (código similar aos outros testes)

# Testes para outros endpoints (habilidades, itens, etc.)

@pytest.mark.slow
def test_performance_pokemon_list():
    """Testa a performance da API ao buscar uma lista grande de Pokémons."""
    # ... (usar um timer para medir o tempo de resposta)

@pytest.fixture
def pokemon_data():
    """Fixture para obter dados de um Pokémon específico."""
    response = requests.get(f"{BASE_URL}pokemon/pikachu")
    return response.json()

def test_pokemon_weight(pokemon_data):
    """Testa o peso do Pokémon utilizando um fixture."""
    assert pokemon_data['weight'] > 0