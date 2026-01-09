import requests
import json
import random

import utils
from utils import get_random_pokemon

#Setup:
# Get the list of 151 Pokémon from the API
url = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"

response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]

pokemon_names = []
for pokemon in pokemon_list:
    pokemon_names.append(pokemon["name"])

player_choice = ""


def menu():
    choice = input("Please choose an option\n1: Choose your pokemon | 2: Random Pokemon\n")
    match choice:
        case "1":
            # Get the user's choice
            input_choice = input("Enter the name of a pokemon").lower()

            # Get the Pokémon's data from the API
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(input_choice)
            response = requests.get(url)
            player_choice = json.loads(response.text)
            print(player_choice)

            #cpu choice
            cpu_choice = get_random_pokemon(pokemon_names, player_choice)

        case "2":
            c = ""
            player_choice = get_random_pokemon(pokemon_names, c)
            cpu_choice = get_random_pokemon(pokemon_names, player_choice)

            print(player_choice)
            print(cpu_choice)



menu()


# Choose random pokemon for CPU player (must not be the same as player chosen pokemon)




# simulate a battle between chosen pokemon -