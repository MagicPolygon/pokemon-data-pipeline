import json
import requests

# pokemon_request_json = requests.get("https://pokeapi.co/api/v2/pokemon/turtwig").json()
# pokemon_species_request_json = requests.get("https://pokeapi.co/api/v2/pokemon-species/turtwig/").json()

# print("pokemon_request_json:")
# print(pokemon_request_json.keys())
# print("pokemon_species_request_json:")
# print(pokemon_species_request_json.keys())

# pokemon = "giratina"
# pokemon_request_status = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}").status_code
# print(pokemon_request_status)
# pokemon_request_json = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}/").json()
# print(pokemon_request_json)
# print("Types:")
# print(pokemon_request_json["types"])
# types = pokemon_request_json["types"]
# print("Type type:")
# print(type(pokemon_request_json["types"]))
# for pokemon_type in types:
#     print(pokemon_type["type"]["name"])

pokemon_list = ["torterra", "dialga", "gliscor", "dusknoir", "bronzong"]
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

print(pokemon_data_dict)




        # types.append(pokemon_type["type"]["name"])
    # pokemon_data.update({pokemon: pokemon_request_json["types"]})
    # pokemon_types =
    # print(f"Pokemon Types: {pokemon_types}")

# print(pokemon_data)

# pokemon_data =

# Is giratina not on here?
