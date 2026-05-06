# pokemon-data-pipeline

## Project description
This project aims to extract data from a Pokémon API, "https://pokeapi.co/", and format the data in a way that Pokémon names, types, and abilities are more easily acccessible.

## Setup instructions
In the terminal, run `pip install requests`.

## How to run the script
After setting up, go to the `pokemon_list` variable in the `Data` section of `pipiline_script.py` and edit the right-hand side so that the list contains the pokemon you are interested in. For example:

`pokemon_list = ["torterra", "dialga", "gliscor", "dusknoir", "bronzong"]`

## Example output
```
{
  "torterra": {
    "name": "torterra",
    "types": [
      "grass",
      "ground"
    ],
    "abilities": [
      "overgrow",
      "shell-armor"
    ]
  },
  "dialga": {
    "name": "dialga",
    "types": [
      "steel",
      "dragon"
    ],
    "abilities": [
      "pressure",
      "telepathy"
    ]
  },
  "gliscor": {
    "name": "gliscor",
    "types": [
      "ground",
      "flying"
    ],
    "abilities": [
      "hyper-cutter",
      "sand-veil",
      "poison-heal"
    ]
  },
  "dusknoir": {
    "name": "dusknoir",
    "types": [
      "ghost"
    ],
    "abilities": [
      "pressure",
      "frisk"
    ]
  },
  "bronzong": {
    "name": "bronzong",
    "types": [
      "steel",
      "psychic"
    ],
    "abilities": [
      "levitate",
      "heatproof",
      "heavy-metal"
    ]
  }
}
```

## Brief explanation of the pipeline
1. The program starts by taking a list of Pokémon from the user and creating an empty Pokémon data dictionary.
2. Then, it does the following for each Pokémon in the list
  1. It inserts the Pokémon's name into the empty dictionary.
  2. It collects the Pokémon's types using the Pokémon API and adds those to a list, which goes in the dictionary in an organised way.
  3. It collects the Pokémon's abilities using the Pokémon API and adds those to a list, which goes in the dictionary in an organised way.
3. After running through the list of Pokémon, it returns the Pokémon data dictionary and updates the data in the `pokemon_data.json` file, which acts as the store of our output.
