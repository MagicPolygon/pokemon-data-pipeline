import json
import requests

# JSON file functions ---------------------------------------------------------------

def write_to_json_file(file_name, data):
    try:
        with open(file_name, "w") as json_file:
            json.dump(data, json_file)
    except:
        print("There was an error with writing the file.")

def load_json_file(file_name):
    try:
        with open(file_name) as json_file:
            data = json.load(json_file)
            return data
    except FileNotFoundError:
        print("There was an error with loading the file: the file does not exist.")

def add_to_json_file(file_name, data):
    try:
        existing_data = load_json_file(file_name)
        existing_data.update(data)
        write_to_json_file(file_name, existing_data)
    except:
        print("There was an error with adding data to the file.")

# Pokémon dictionary functions -------------------------------------------------------

def enter_pokemon_data(pokemon_list):
    try:
        pokemon_data_dict = {}

        for pokemon in pokemon_list:
            pokemon_data_dict.update({pokemon: {}})
            pokemon_data_dict = insert_pokemon_name(pokemon_data_dict, pokemon)
            pokemon_data_dict = insert_pokemon_type(pokemon_data_dict, pokemon)
            pokemon_data_dict = insert_pokemon_abilities(pokemon_data_dict, pokemon)

        return pokemon_data_dict
    except:
        print("There was an error with entering pokemon data to the pokemon data dictionary.")

def insert_pokemon_name(pokemon_data_dict, pokemon):
    try:
        # print(f"Pokemon Name: {pokemon}")
        pokemon_data_dict[pokemon]["name"] = pokemon
        return pokemon_data_dict
    except:
        print("There was an error with inserting pokemon names to the pokemon data dictionary.")

def insert_pokemon_type(pokemon_data_dict, pokemon):
    try:
        types = []
        pokemon_request_json = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()
        for index, pokemon_type in enumerate(pokemon_request_json["types"]):
            # print(f"Type {index + 1}: {pokemon_type["type"]["name"]}")
            types.append(pokemon_type["type"]["name"])

        pokemon_data_dict[pokemon]["types"] = types

        return pokemon_data_dict
    except:
        print("There was an error with inserting pokemon types to the pokemon data dictionary.")

def insert_pokemon_abilities(pokemon_data_dict, pokemon):
    try:
        abilities = []
        pokemon_request_json = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()
        for index, pokemon_ability in enumerate(pokemon_request_json["abilities"]):
            # print(f"Ability {index + 1}: {pokemon_ability["ability"]["name"]}")
            abilities.append(pokemon_ability["ability"]["name"])

        pokemon_data_dict[pokemon]["abilities"] = abilities

        return pokemon_data_dict
    except:
        print("There was an error with inserting pokemon abilities to the pokemon data dictionary.")

# Data -------------------------------------------------------------------------------

file_name = "pokemon_data.json"
pokemon_list = []
pokemon_data_dict = enter_pokemon_data(pokemon_list)

# Processing -------------------------------------------------------------------------

# print(pokemon_data_dict)

add_to_json_file(file_name, pokemon_data_dict)





