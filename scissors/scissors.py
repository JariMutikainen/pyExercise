# This program makes you play rock-paper-scissors game against the computer.
print("Let's play rock-paper-scissors!")
good_answer = False
while not good_answer:
    human = input("Choose Rock = 'r', Paper = 'p' or Scissors = 's': ")
    if human == "r" or human == "p" or human == "s":
        good_answer = True
    else:
        print("Illegal input. Try again.")

from random import randint
computer = randint(0,2) # Generates an integer in the range of 0-2
# Convert the random number into rock, paper or scissors
if computer == 0:
    computer = "r"
elif computer == 1:
    computer = "p"
else:
    computer = "s"

print(f"Computer selected {computer}")
if human == "r":
    if computer == "r":
        print("Nobody wins. It is a tie!")
    elif computer == "p":
        print("You loose.")
    else: # computer selected "s"
        print("You win.")
elif human == "p":
    if computer == "r":
        print("You win.")
    elif computer == "p":
        print("Nobody wins. It is a tie!")
    else: # computer selected "s"
        print("You loose.")
else: # Human selected "s"
    if computer == "r":
        print("You loose.")
    elif computer == "p":
        print("You win.")
    else: # computer selected "s"
        print("Nobody wins. It is a tie!")

