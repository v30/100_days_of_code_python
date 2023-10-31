# Welcome
import random

heads_tails = ["HEADS", "TAILS"]
play = True
print("Let's play HEADS or TAILS...")


def flip_coin():
    global play
    while play:
        ans = input("Flip the coin? ")
        if ans == "y" or ans == "Y":
            num = random.randint(0, 1)
            print(heads_tails[num])
        else:
            print("Goodbye!")
            play = False


flip_coin()

