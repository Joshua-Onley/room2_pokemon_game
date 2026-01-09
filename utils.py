import random

def get_random_pokemon(pokemon_names: list, player_choice: str) -> str:
    random_pokemon = player_choice
    while random_pokemon == player_choice:
        random_pokemon = random.choice(pokemon_names)

    return random_pokemon
