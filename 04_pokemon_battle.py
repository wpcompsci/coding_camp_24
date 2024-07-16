import random
import time


def battle(player_name, player_health, cpu_name, cpu_health):
    # NAME PLAYERS
    if player_name == "1":
        player_name = "Pikachu"
    elif player_name == "2":
        player_name = "Charizard"
    else:
        player_name = "Bulbasaur"

    if cpu_name == "1":
        cpu_name = "Pikachu"
    elif cpu_name == "2":
        cpu_name = "Charizard"
    else:
        cpu_name = "Bulbasaur"


    # SETUP ATTACKS
    if player_name == "Pikachu":
        player_attacks = ["Thunder Shock", "Quick Attack", "Thunderbolt"]
    elif player_name == "Charizard":
        player_attacks = ["Flamethrower", "Fire Spin", "Fire Blast"]
    else:
        player_attacks = ["Vine Whip", "Razor Leaf", "Solar Beam"]

    if cpu_name == "Pikachu":
        cpu_attacks = ["Thunder Shock", "Quick Attack", "Thunderbolt"]
    elif cpu_name == "Charizard":
        cpu_attacks = ["Flamethrower", "Fire Spin", "Fire Blast"]
    else:
        cpu_attacks = ["Vine Whip", "Razor Leaf", "Solar Beam"]

    print(f"{player_name} vs. {cpu_name}!")

    while True:
        print(f"{player_name}: {player_health} HP")
        print(f"{cpu_name}: {cpu_health} HP")

        time.sleep(1)

        print("\nYour turn!")
        print("Choose your attack:")
        for i, attack in enumerate(player_attacks, 1):
            print(f"{i}. {attack}")

        player_attack = int(input("Enter the number of your attack: "))

        time.sleep(1)

        if player_attack == 1:
            print(f"{player_name} used {player_attacks[0]}!")
            time.sleep(1)
            damage = random.randint(10, 15)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        elif player_attack == 2:
            print(f"{player_name} used {player_attacks[1]}")
            time.sleep(1)
            damage = random.randint(5, 20)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        elif player_attack == 3:
            print(f"{player_name} used {player_attacks[2]}")
            time.sleep(1)
            damage = random.randint(0, 30)
            cpu_health -= damage
            print(f"{cpu_name} took {damage} damage!")
        else:
            time.sleep(1)
            print("You missed!")

        time.sleep(1)

        if cpu_health <= 0:

            print(f"{cpu_name} fainted!")
            break

        print(f"\n{cpu_name}'s turn!")

        cpu_attack = random.randint(1, 3)

        time.sleep(1)

        if cpu_attack == 1:
            print(f"{cpu_name} used {cpu_attacks[0]}")
            time.sleep(1)
            damage = random.randint(10, 15)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")
        elif cpu_attack == 2:
            print(f"{cpu_name} used {cpu_attacks[1]}")
            time.sleep(1)
            damage = random.randint(5, 20)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")
        elif cpu_attack == 3:
            print(f"{cpu_name} used {cpu_attacks[2]}")
            time.sleep(1)
            damage = random.randint(0, 30)
            player_health -= damage
            print(f"{player_name} took {damage} damage!")

        time.sleep(1)

        if player_health <= 0:
            print(f"{player_name} fainted!")
            break

        print("\nNext round!")

    print("\nBattle over!")
    if player_health <= 0:
        print(f"{cpu_name} wins!")
    else:
        print(f"{player_name} wins!")

# START THE PROGRAM

print("Choose your Pokemon!")
print("1. Pikachu")
print("2. Charizard")
print("3. Bulbasaur")

player_character = input("Select a number: ")

print("\nChoose your opponent!")
print("1. Pikachu")
print("2. Charizard")
print("3. Bulbasaur")

cpu_character = input("Select a number: ")

battle(player_character, 40, cpu_character, 40)
