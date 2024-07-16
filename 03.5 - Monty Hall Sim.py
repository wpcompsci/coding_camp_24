import random

print("Welcome to the Monty Hall Simulation!")

input("\nPress Enter to start the simulation.\n")

stick_wins = 0
switch_wins = 0
tries = int(input("How many times would you like to run the simulation? "))

for i in range(tries):
    winning_door = random.randint(1, 3)
    chosen_door = random.randint(1, 3)

    if winning_door == chosen_door:
        stick_wins += 1
    else:
        switch_wins += 1

print(f"\nAfter {tries} simulations:")
print(f"Sticking with the original door wins {stick_wins} times.")
print(f"Switching doors wins {switch_wins} times.")
print(f"Sticking wins {stick_wins / tries * 100:.2f}% of the time.")
print(f"Switching wins {switch_wins / tries * 100:.2f}% of the time.")
