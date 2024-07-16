import random

print("Welcome to Guess My Number!")

input("\nPress Enter to start the game.\n"
      "The current low score is 1,000,000,000,000,000 attempts.\n")

correct_number = random.randint(1, 100)
guess = 0
attempts = 0
low_score = 1_000_000_000_000_000

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 100: "))
    attempts = attempts + 1

    if guess < correct_number:
        print("Your guess is too low.")
    elif guess > correct_number:
        print("Your guess is too high.")
    else:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        if attempts < low_score:
            low_score = attempts
            print(f"New low score! {low_score} attempts.")