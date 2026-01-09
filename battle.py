def battle(player, cpu):
    print(f"{player['name']} VS {cpu['name']}")

    player_score = player["hp"] + player["attack"]
    cpu_score = cpu["hp"] + cpu["attack"]

    if player_score > cpu_score:
        print(f"{player['name']} wins!")
    elif cpu_score > player_score:
        print(f"{cpu['name']} wins!")
    else:
        print("It's a draw!")