# Playing with the random module

import random

# random.seed(1)
play_again = True


def rock_paper_scissors():
    global play_again
    score_player = 0
    score_cpu = 0

    while play_again:
        i = random.randint(1, 3)
        opt = input("(R)ock, (P)aper, (S)cissor? ")

        if opt == "R" or opt == "r":
            if i == 1:
                print("Tie!")
            elif i == 2:
                print("You lose!")
                score_cpu += 1
            else:
                print("You win!")
                score_player += 1
        elif opt == "P" or opt == "p":
            if i == 1:
                print("You win!")
                score_player += 1
            elif i == 2:
                print("Tie!")
            else:
                print("You lose!")
                score_cpu += 1
        elif opt == "S" or opt == "s":
            if i == 1:
                print("You lose!")
                score_cpu += 1
            elif i == 2:
                print("You win!")
                score_player += 1
            else:
                print("Tie!")
        else:
            print("Invalid Option! ")

        if i == 1:
            print("CPU picked Rock!")
        elif i == 2:
            print("CPU picked Paper!")
        else:
            print("CPU picked Scissor!")

        print("SCORE")
        print(f"Player: {score_player}\t\t\tCPU: {score_cpu}")
        ans = input("Play again? Y or N: ")
        if ans == "N" or ans == "n":
            play_again = False


rock_paper_scissors()
