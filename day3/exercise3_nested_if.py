print("Welcome to exercise 3.")
number = int(input("Enter a number to check odd/even and >10: "))

if number % 2 == 0:
    if number > 10:
        print(f"{number} is even and is > 10")
    else:
        print(f"{number} is even but is < 10")
else:
    if number > 10:
        print(f"{number} is odd and is > 10")
    else:
        print(f"{number} is odd but is < 10")
