import requests
import json
from utils import get_random_pokemon


def menu():
    pass


# Get the list of pokemon from the API
url = "https://pokeapi.co/api/v2/pokemon/"
response = requests.get(url)
pokemon_list = json.loads(response.text)["results"]

for pokemon in pokemon_list:
    print(pokemon["name"])

# Ask the user to choose a pokemon
print("Enter your pokemon:")

# Get the user's choice
choice = input().lower()

# Get the pokemon's data from the API
url = "https://pokeapi.co/api/v2/pokemon/{}/".format(choice)
response = requests.get(url)
pokemon_data = json.loads(response.text)

# to get ability
abilities = pokemon_data["abilities"][0]
ability = abilities["ability"]

# to format height and weight properly
height = int(pokemon_data["height"])
weight = int(pokemon_data["weight"])

height_formatted = height / 10
weight_formatted = weight / 10

# Print the pokemon's data
print("Name: {}".format(pokemon_data["name"]))
print("Weight: {}".format(weight_formatted) + "(kgs)")
print("Height: {}".format(height_formatted) + "(m)")
print("Ability: {}".format(ability["name"]))


# Choose random pokemon for CPU player (must not be the same as player chosen pokemon)
import random

pokemon_names = []
for pokemon in pokemon_list:
    pokemon_names.append(pokemon["name"])
print(f"pokemon_names: {pokemon_names}")

cpu_player = choice
while cpu_player == choice:
    cpu_player = random.choice(pokemon_names)

print(f"The CPU player selects {cpu_player}")


# simulate a battle between chosen pokemon -


#
