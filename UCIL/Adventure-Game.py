# --- My Adventure Game --- #
print("Welcome to my game!")

pName = input("What is your name? ")
print(f"Hello, welcome to the adventure, {pName}!")

print("Choose a character", "1. Knight", "2. Elf", "3. Wizard", sep = '\n')

characterList = ["Knight", "Elf", "Wizard"]

character = input("Type in your character number: ")

print(pName, "You chose the", characterList[int(character)-1])

gameStarted = True
commandList = ['GameStart!', 'exit', 'actions', 'items', 'Inventory']

InventryList = ["backpack", "water bottle", "length of rope", "food"]

HealthStat = 10
Event = ['Enemy', 'Treasure box', 'Coin', 'Animal']

import random

while gameStarted:
    command = input("input your command: ")
    if command == "Inventory":
        print(InventryList)
    if command == "GameStart!":
        print("You are entering the forest...")
        situation = Event[random.randint(0, 3)]
        print("You encountered", situation, "!")
        if situation == 'Enemy':
            print("you loose HP: HP-1")
            HealthStat = HealthStat - 1
            print("Current HP:", HealthStat)

