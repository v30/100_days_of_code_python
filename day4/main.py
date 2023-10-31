print("Hi, welcome...")
print("1. Rock, paper, scissors")
print("2. Heads or Tails")
option = int(input("Let's play: "))

if option == 1:
    import random_test
    random_test.rock_paper_scissors()
else:
    import head_tails
    head_tails.flip_coin()