# Terminal RPG

A text-based RPG built in Python featuring turn-based combat, player progression, enemy encounters, and persistent save data using JSON.

## 🎮 Overview

Terminal RPG is a lightweight command-line game where the player battles enemies, gains levels, and tracks progress across sessions. The game focuses on basic RPG mechanics and system design using Python.

## ⚙️ Features

- Turn-based combat system
- Reaction-time based attack/defense mechanic
- Player stats (Strength, Agility)
- Enemy system with HP and damage
- Level progression system
- Kill count and high score tracking
- Persistent data storage using JSON
- Multi-file modular structure

## 🧠 Core Mechanics

- Players attack enemies to reduce HP
- Enemies retaliate during combat turns
- Faster reactions can reduce incoming damage
- Defeating enemies increases kill count
- Level up system improves player stats
- High score tracks best performance per player

## 💾 Save System

Player data is stored in a JSON file (`plyr.json`) which includes:

- Username data
- Progression (Level, Damage, Highscore)
- Stats (Strength, Agility)

> Note: Save file is automatically read and updated during gameplay.

## 📁 Project Structure
- main.py → Starts the game and runs the main loop
- gameplay.py → Handles story flow, levels, and game progression
- fight.py → Manages combat system (attacks, turns, timing)
- player.py → Player class (stats, actions, progression logic)
- enemy.py → Enemy class (HP, damage, behavior)
- plyerdata.py → Handles saving and loading player data (JSON system)
- plyr.json → Save file that stores player progress

## 🚀 How to Run

1. Make sure Python 3 is installed
2. Clone the repository:
   ```bash
   git clone <repo-url>

## Run the game
python main.py

⚠️ Notes
This is a Version 1 prototype project.
Some systems are experimental and may change in future versions.
Designed as a learning project for Python, OOP, and system design.
