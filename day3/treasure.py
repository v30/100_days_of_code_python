print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice = input("Do you want to go (L)eft or (R)ight? ")
if choice == "r":
    print("You are attacked by crazy monkeys. Game Over!!!")
elif choice == "l":
    print("You get to a river")
    choice = input("Are you going to (S)wim or (W)ait for a boat? ")
    if choice == "s":
        print("You get attacked by a crocodiles. Game Over!!!")
    elif choice == "w":
        print("You come to 3 doors.")
        choice = input("Which one are you going to take? (R)ed, (Y)ellow or (B)lue? ")
        if choice == "r":
            print("The room is on fire, you get burned alive. Game Over!")
        elif choice == "b":
            print("You fall into the ocean and you are attacked by a shark. Game Over!")
        elif choice == "y":
            print("You have found the treasure. Congratulations... YOU WIN!")
        else:
            print("Game Over!!!")
    else:
        print("Game Over!!!")
else:
    print("Game Over!!!")