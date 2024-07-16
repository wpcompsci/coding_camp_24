import random
import time

print("Welcome to the Magic 8 Ball!")
print("Ask me a question and I will predict the future.")

input("\nWhat is your question? ")

print(f"The Magic 8 Ball is thinking", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)
print(".", end="")
time.sleep(1)

input("\nPress Enter to reveal the answer.\n")

response = random.randint(1, 8)

if response == 1:
    print("Yes.")
elif response == 2:
    print("No.")
elif response == 3:
    print("Maybe.")
elif response == 4:
    print("Ask again later.")
elif response == 5:
    print("It is certain.")
elif response == 6:
    print("It is decidedly so.")
elif response == 7:
    print("Most likely.")
else:
    print("Outlook not so good.")