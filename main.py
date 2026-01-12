import requests
import json
import random
from utils import get_random_pokemon
import battle


# Setup:
# Get the list of 151 Pokémon from the API
url = "https://pokeapi.co/api/v2/pokemon?limit=151&offset=0"
response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]

pokemon_names = []
for pokemon in pokemon_list:
    pokemon_names.append(pokemon["name"])

player_choice = ""


def menu():
    choice = input(
        "Please choose an option\n1: Choose your pokemon | 2: Random Pokemon\n"
    )
    match choice:
        case "1":
            # Get the user's pokemon choice
            player_choice = input("Enter the name of a pokemon: ").lower()

            # Get the Pokémon's data from the API
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(player_choice)
            response = requests.get(url)
            player_choice = json.loads(response.text)

            # generate random choice for the cpu pokemon
            cpu_choice = get_random_pokemon(pokemon_names, player_choice)

            cpu_url = "https://pokeapi.co/api/v2/pokemon/{}/".format(cpu_choice)
            cpu_response = requests.get(cpu_url)
            cpu_pokemon_details = json.loads(cpu_response.text)

            result = battle.simulate_battle(cpu_pokemon_details, player_choice)

            if result == "draw":
                print("The battle is a draw!")
            else:
                print(f"Winner of the battle: {result}")

        case "2":
            # get a random pokemon from the list of pokemon names and assign it to the player
            player_choice = get_random_pokemon(pokemon_names, "")

            # get a random pokemon from the list of pokemon names and assign it to cpu
            # avoids picking the same pokemon as player choice (second parameter)
            cpu_choice = get_random_pokemon(pokemon_names, player_choice)

            # fetches information about the randomly chosen cpu pokemon and formats it as a dictionary
            cpu_url = "https://pokeapi.co/api/v2/pokemon/{}/".format(cpu_choice)
            cpu_response = requests.get(cpu_url)
            cpu_pokemon_details = json.loads(cpu_response.text)

            # fetches information about the randomly chosen player pokemon and formats it as a dictionary
            url = "https://pokeapi.co/api/v2/pokemon/{}/".format(player_choice)
            response = requests.get(url)
            player_pokemon_details = json.loads(response.text)

            # passes player pokemon dictionary and cpu pokemon dictionary to a function
            # that determines the winner based on information in the dictionaries
            result = battle.simulate_battle(
                cpu_pokemon_details, player_pokemon_details
            )

            if result == "draw":
                print("The battle is a draw!")
            else:
                print(f"Winner of the battle: {result}")


menu()
