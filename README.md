#   Pokémon Battle Game

##  Project Overview
This is a simple Python Pokémon battle game that uses the **PokéAPI** to fetch real Pokémon data.

The game randomly assigns a Pokémon to the player and the CPU, then compares their stats to decide a winner.

This project focuses on:  
- Using an external API  
- Working collaboratively using GitHub  
- Writing clean, modular Python code  

---

##  Technologies Used
- Python  
- PokéAPI ([https://pokeapi.co](https://pokeapi.co))  
- requests library  

---

## 📂 Project Structure
pokemon-game/
├── main.py
├── pokemon_api.py
├── battle.py
└── README.md

## 📝 Menu / Options
- **Choose a Pokémon** – Player can pick their Pokémon  
- **Get a random Pokémon** – Player gets a random Pokémon to battle  
- **CPU Pokémon** – CPU is assigned a random Pokémon each time  
- **Start Battle** – Begin the fight between player and CPU Pokémon
  


**File explanation:**
- `main.py` → Controls the game flow  
- `pokemon_api.py` → Fetches Pokémon data from the API  
- `battle.py` → Handles the battle logic  
- `README.md` → Project documentation  

##  Issues / Known Bugs
- Repository had to be recreated because **branch protection on the main branch was not working correctly**  
- Accidental commits from feature branches could have caused **merge conflicts**, so branch rules were adjusted for safe collaboration  

---

##   How to Run the Game

###  Install dependencies
Make sure you have Python installed, then run:
pip install requests


---

##   How the Game Works
1. The game starts and welcomes the player  
2. A random Pokémon is assigned to the player  
3. A random Pokémon is assigned to the CPU  
4. The Pokémon battle using their stats  
5. A winner (or draw) is displayed  

---

##  Battle Logic
The winner is decided by comparing:  
- **HP**  
- **Attack**  

The Pokémon with the higher combined score wins.

---

##  Collaboration
This project was designed to be worked on by **2–3 collaborators**:
- One person works on API logic  
- One person works on battle logic  
- One person manages the main game flow  

GitHub branches and pull requests were used to collaborate safely.

---

##  Future Improvements
- Allow player to choose their Pokémon  
- Add abilities or type advantages  
- Add turn-based battles  
- Add two-player mode  

---

##  Learning Outcomes
- Understand how to use an **external API**  
- Practice **functions and modules**  
- Work collaboratively using **Git**  
- Build a simple but complete Python project
