# --- My Adventure Game --- #
import json, os # os = operating system
print("Welcome to my game!")

have_save = os.path.exists("player_data.json")
load_save = False

if have_save:
    load_choice = input("Would you like to load your saved progress? y/n").lower()
    if load_choice == "y":
        load_save = True
    # elif load_choice == 'n':
    #     load_save = False

if load_save:
    with open("player_data.json", "r") as file:
        player_data = json.load(file)

    playerName = player_data["name"]
    character = player_data["character"]
    health = player_data["health"]
    inventory = player_data["inventory"]

    print(f"Welcome back {playerName}, the {character}!")
    print(f"Health: {health}")
    print("Your inventory: ")
    for item, quantity in inventory.items():
        print(f"  - {item}: {quantity}")

else:
    playerName =input("What is your name? ")
    print("Welcome to the adventure, ", playerName)
    print("Please choose a character: 1. Knight, 2. Elf, 3. Wizard", sep = "\n")

    characterList = ["Knight", "Elf", "Wizard"]
    chosenCharacter = input("Type in the character number: ")
    character = characterList[int(chosenCharacter) - 1]
    print("Welcome", playerName, "you are a", character)

    inventory = {
        "Backpack": 1,
        "Water Bottle": 1,
        "Rope": 1,
        "Food": 3
    }

    character_items = {
        "Knight": {"Sword": 1, "Shield": 1, "Armor": 1},
        "Elf": {"Bow": 1, "Arrows": 20, "Cloak": 1},
        "Wizard": {"Staff": 1, "Spellbook": 1, "Potion": 3}
    }
    
    if character in character_items:
        for item, quantity in character_items[character].items():
            inventory[item] = quantity
    
    health = 100
    player_data = {
        "name": playerName,
        "character": character,
        "health": health,
        "inventory": inventory
    }

    with open("player_data.json", "w") as file:
        json.dump(player_data, file, indent = 2)
    print("New game saved successfully!")


elif action == "fight":
    player()


# gameStarted = True
# commandList = ['exit', 'actions', 'items']

# itemsKnight = ["Sword", "Shield"]
# itemsElf = ["Bows", "Gifts"]
# itemsWizard = ["Wands", 'Staff']

# while gameStarted:
#     command = input("input your command: ")
#     if command == "actions":
#         print(commandList)
#     if command == "exit":
#         print("You quit the game!")
#         break
#         # or you can use this line:
#         # gameStarted = False
#     if command == "items":
#         if characterList[int(character)-1] == "Knight":
#             print(itemsKnight)
#         if characterList[int(character)-1] == "Elf":
#             print(itemsElf)
#         if characterList[int(character)-1] == "Wizard":
#             print(itemsWizard)

