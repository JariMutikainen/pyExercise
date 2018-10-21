# Asks the user to guess repeatedly, what the random number in the range of
# 1 - 10 selected by the computer is.
import random
play_again = True
while play_again:
    ran = random.randint(1,10)
    num = int(input("Guess my random number in the " + 
                     "range of 1-10 (inclusive): "))
    if num == ran:
        print("You got that right!")
    else:
        while num != ran:
            if num < ran:
                print(f"No, it is larger than {num}. Try again.")
            else: # num > ran
                print(f"No, it is smaller than {num}. Try again.")
            num = int(input("What is your next guess: "))
        print(f"Congratulations. It is {num} indeed.")
    answ = input("Do you want to play again (y/n)? : ")
    if answ == "y":
        play_again = True
    else:
        play_again = False


