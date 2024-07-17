# GLOBAL VARIABLES
inventory = []


def valid_input(prompt, options):
    while True:
        choice = input(prompt).upper()
        if choice in options:
            return choice
        else:
            print("Invalid input. Please try again.")


def old_oak():
    print("You have arrived at the old oak. \n"
          "The tree is massive and ancient. \n"
          "One of the branches is low enough to climb. \n"
          "You can see an acorn hanging up there.")

    prompt = ("What would you like to do? \n"
              "A. Climb the tree and get the acorn?\n"
              "B. Leave the tree and continue on your path?\n")
    options = ["A", "B"]

    choice = valid_input(prompt, options)

    if choice == "A":
        if "Acorn" in inventory:
            print("You already have the acorn.")
        else:
            print("You climb the tree and get the acorn.")
            inventory.append("Acorn")
        old_oak()
    else:
        print("You leave the tree and continue on your path.")
        prompt = ("Where would you like to go next? \n"
                  "A. Rainbow Falls\n"
                  "B. Happy Trails\n")
        options = ["A", "B"]
        choice = valid_input(prompt, options)

        if choice == "A":
            rainbow_falls()
        else:
            happy_trails()


def rainbow_falls():
    print("You have arrived at Rainbow Falls. \n"
          "The waterfall is beautiful and the mist is refreshing. \n"
          "You can see a rainbow in the mist.")

    prompt = ("What would you like to do? \n"
              "A. Walk through the mist and see the rainbow up close?\n"
              "B. Leave the falls and continue on your path?\n")
    options = ["A", "B"]
    choice = valid_input(prompt, options)

    if choice == "A":
        print("You walk through the mist and see the rainbow up close.")
        rainbow_falls()
    else:
        print("You leave the falls and continue on your path.")
        prompt = ("Where would you like to go next? \n"
                  "A. Old Oak\n"
                  "B. Happy Trails\n")
        options = ["A", "B"]
        choice = valid_input(prompt, options)

        if choice == "A":
            old_oak()
        else:
            happy_trails()


def happy_trails():
    print("You have arrived at Happy Trails. \n"
          "The path is lined with flowers and butterflies. \n"
          "You can see a bunny hopping along the path.")

    prompt = ("What would you like to do? \n"
              "A. Follow the bunny and see where it goes?\n"
              "B. Leave the path and continue on your journey?\n")
    options = ["A", "B"]
    choice = valid_input(prompt, options)

    if choice == "A":
        print("You follow the bunny and see where it goes.")
        print("The bunny leads you to a field of super evil bunnies.")

        prompt = ("What would you like to do? \n"
                  "A. Run away?\n"
                  "B. Fight the super evil bunnies?\n")
        options = ["A", "B"]
        choice = valid_input(prompt, options)

        if choice == "A":
            print("You run away from the super evil bunnies.")
            happy_trails()
        else:
            print("You fight the super evil bunnies.")
            if "Acorn" in inventory:
                print("You use the acorn to defeat the super evil bunnies.")
                print("You have defeated the super evil bunnies!")
                end_game("win")
            else:
                print("The super evil bunnies are too powerful. You are defeated.")
                end_game("lose")
    else:
        print("You leave the path and continue on your journey.")
        prompt = ("Where would you like to go next? \n"
                  "A. Old Oak\n"
                  "B. Rainbow Falls\n")
        options = ["A", "B"]
        choice = valid_input(prompt, options)

        if choice == "A":
            old_oak()
        else:
            rainbow_falls()


def end_game(outcome):
    if outcome == "win":
        print("Congratulations! You have completed the adventure!")
    else:
        print("Game Over. Better luck next time.")

    play_again = input("Would you like to play again? (Y/N) ").upper()

    if play_again == "Y":
        inventory.clear()
        old_oak()
    else:
        print("Thank you for playing. Goodbye!")


old_oak()
