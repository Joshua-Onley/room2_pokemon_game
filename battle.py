def simulate_battle(cpu: dict, player: dict) -> str:
    player_pokemon_height = player["height"]
    player_pokemon_name = player["name"]
    cpu_pokemon_height = cpu["height"]
    cpu_pokemon_name = cpu["name"]

    print(
        f"simulating battle between {player_pokemon_name} (player) and {cpu_pokemon_name} (cpu)"
    )
    print(f"height of {player_pokemon_name}: {player_pokemon_height}")
    print(f"height of {cpu_pokemon_name}: {cpu_pokemon_height}")

    if cpu_pokemon_height > player_pokemon_height:
        print("CPU Wins")
        return cpu_pokemon_name
    elif player_pokemon_height > cpu_pokemon_height:
        print("Player wins")
        return player_pokemon_name
    else:
        return "draw"

    """
    print(f"{player['name']} VS {cpu['name']}")

    player_score = player["hp"] + player["attack"]
    cpu_score = cpu["hp"] + cpu["attack"]

    if player_score > cpu_score:
        print(f"{player['name']} wins!")
    elif cpu_score > player_score:
        print(f"{cpu['name']} wins!")
    else:
        print("It's a draw!")
"""
