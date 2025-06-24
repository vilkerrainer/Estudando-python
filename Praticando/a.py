import requests

def get_pokemon_type(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        types = [t['type']['name'] for t in data['types']]
        return types
    else:
        return None
    

def get_pokemon_abilities(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        abilities = [t['ability']['name'] for t in data['abilities']]
        return abilities
    else:
        return None


def get_pokemon_weight(pokemon_name):

    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)    
    if response.status_code == 200:
        data = response.json()
        weights = data['weight']
        return  weights
    else:
        return None

# Exemplo de uso:
pokemon = "gengar"

types = get_pokemon_type(pokemon)
weight = get_pokemon_weight(pokemon)
abilities = get_pokemon_abilities(pokemon)



if types and weight and abilities:
    print(f"Types of {pokemon.capitalize()}: {', '.join(types)}")
    print(f"The weight of pokemon {pokemon.capitalize()} is {weight}")
    print(f"Abilities of {pokemon.capitalize()}: {', '.join(abilities)}")
else:
    print("Pokémon não encontrado!")