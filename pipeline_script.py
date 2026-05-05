import json
import requests

# JSON file functions ---------------------------------------------------------------

def write_to_json_file(file_name, data):
    with open(file_name, "w") as json_file:
        json.dump(data, json_file)

def load_json_file(file_name):
    with open(file_name) as json_file:
        data = json.load(json_file)
        return data

def add_to_json_file(file_name, data):
    existing_data = load_json_file(file_name)
    existing_data.update(data)
    write_to_json_file(file_name, existing_data)

# Other functions --------------------------------------------------------------------

def enter_pokemon_data(pokemon_list):
    pokemon_data_dict = {}

    for pokemon in pokemon_list:
        pokemon_data = {}
        pokemon_data_dict.update({pokemon: pokemon_data})
        pokemon_request_json = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()

        # Inserting pokemon name
        print(f"Pokemon Name: {pokemon}")
        pokemon_data_dict[pokemon]["name"] = pokemon

        # Inserting pokemon types
        types = []
        for index, pokemon_type in enumerate(pokemon_request_json["types"]):
            print(f"Type {index + 1}: {pokemon_type["type"]["name"]}")
            types.append(pokemon_type["type"]["name"])

        pokemon_data_dict[pokemon]["types"] = types

        # Inserting pokemon abilities
        abilities = []
        for index, pokemon_ability in enumerate(pokemon_request_json["abilities"]):
            print(f"Ability {index + 1}: {pokemon_ability["ability"]["name"]}")
            abilities.append(pokemon_ability["ability"]["name"])

        pokemon_data_dict[pokemon]["abilities"] = abilities

    return pokemon_data_dict

# Data -------------------------------------------------------------------------------

file_name = "pokemon_data.json"
pokemon_list = ["torterra", "dialga", "gliscor", "dusknoir", "bronzong"]
pokemon_data_dict = enter_pokemon_data(pokemon_list)

# Processing -------------------------------------------------------------------------

print(pokemon_data_dict)

add_to_json_file(file_name, pokemon_data_dict)





