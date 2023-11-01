# Inputs
import random

num_chars = int(input("How long should the password be? "))
num_special = int(input("How many special characters should it have? "))
num_numerical = int(input("Hom many number characters should it contain? "))

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v",
           "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R",
           "S", "T", "U", "V", "W", "X", "Y", "Z"]
specials = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "=", "+"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

password = ""
count_spec = 0
count_nums = 0

while len(password) < num_chars:
    rnd_list = random.randint(0, 2)
    if rnd_list == 0:
        rnd = random.randint(0, len(letters) - 1)
        password += letters[rnd]
    elif rnd_list == 1 and count_spec < num_special:
        rnd = random.randint(0, len(specials) - 1)
        password += specials[rnd]
        count_spec += 1
    elif rnd_list == 2 and count_nums < num_numerical:
        rnd = random.randint(0, len(numbers) - 1)
        password += numbers[rnd]
        count_nums += 1

print(password)