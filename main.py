"""
Pokemon Collection with Dictionaries
"""

import os

# Dictionary to store Pokemon data
PC_Box = {
    "Arceus" : {
        "Type" : "Normal",
        "Level" : 100,
        "HP" : 414
    },
    "Dialga" : {
        "Type" : "Steel",
        "Level" : 90,
        "HP" : 364
    },
    "Palkia" : {
        "Type" : "Water",
        "Level" : 90,
        "HP" : 346
    },
    "Giratina" : {
        "Type" : "Ghost",
        "Level" : 90,
        "HP" : 398
    },
    "Mew" : {
        "Type" : "Psychic",
        "Level" : 50,
        "HP" : 151
    },
    "Bidoof" : {
        "Type" : "Normal",
        "Level" : 80,
        "HP" : 258
    },
    "Articuno" : {
        "Type" : "Ice",
        "Level" : 70,
        "HP" : 323
    },
    "Zapdos" : {
        "Type" : "Electric",
        "Level" : 70,
        "HP" : 304
    },
    "Moltres" : {
        "Type" : "Fire",
        "Level" : 70,
        "HP" : 312
    },
    "Ho-Oh" : {
        "Type" : "Fire",
        "Level" : 70,
        "HP" : 327
    }
}

# Function to add a new Pokemon to the collection
def add_pokemon():
    name = input("Enter the name of the Pokemon: ")
    type = input("Enter the type of the Pokemon: ")
    level = int(input("Enter the level of the Pokemon: "))
    hp = int(input("Enter the HP of the Pokemon: "))
    PC_Box[name] = {
        "Type" : type,
        "Level" : level,
        "HP" : hp
    }

# Function to change the stats of an existing Pokemon
def change_stats():
    name = input("Enter the name of the Pokemon: ").lower().capitalize()
    if name in PC_Box:
        print(f"Current stats for {name}: {PC_Box[name]}")
        stat = input("Enter the stat you want to change (Type, Level, HP): ").lower()

        if stat == "type":
            new_type = input("Enter the new type: ").lower().capitalize()
            PC_Box[name]["Type"] = new_type

        elif stat == "level":
            new_level = int(input("Enter the new level: "))
            PC_Box[name]["Level"] = new_level

        elif stat == "hp":
            new_hp = int(input("Enter the new HP: "))
            PC_Box[name]["HP"] = new_hp

        else:
            print("Invalid stat")

        PC_Box[name] = {
            "Type" : PC_Box[name]["Type"],
            "Level" : PC_Box[name]["Level"],
            "HP" : PC_Box[name]["HP"]
        }
    else:
        print("Pokemon not found in PC Box")

# Function to release a Pokemon from the collection
def release_pokemon():
    name = input("Enter the name of the Pokemon: ")
    if name in PC_Box:
        del PC_Box[name]
        print(f"{name} has been released from the PC Box")
    else:
        print("Pokemon not found in PC Box")

# Function to view all Pokemon in the box
def view_all_pokemon():
    for pokemon, stats in PC_Box.items():
        print(f"\nName: {pokemon}")
        print(f"  Type: {stats['Type']}")
        print(f"  Level: {stats['Level']}")
        print(f"  HP: {stats['HP']}")

option = ""
while option != "5":
    # Display menu options
    print("Select an option: \n1. Add Pokemon \n2. Change Stats \n3. Release Pokemon \n4. View All Pokemon \n5. Exit Box")
    option = input(">> ")

    if option == "1":
        add_pokemon()

    elif option == "2":
        change_stats()

    elif option == "3":
        release_pokemon()

    elif option == "4":
        view_all_pokemon()  

    elif option == "5":
        print("Goodbye!")  # Exit the program
        break
    else:
        print("Invalid option")  # Handle invalid menu option
    
    input("Press enter to continue...")  # Wait for user input before clearing the screen
    os.system("cls" if os.name == "nt" else "clear")  # Clear the screen