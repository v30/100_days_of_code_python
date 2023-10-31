# Get a random name from a list of names
import random
print("Welcome to Random name from List")

name_string = input("Input your list of names seperated by \", \": ")
names = name_string.split(", ")

print(F"Random name: {names[random.randint(0, len(names) - 1)]}")

lst = [["ASDF", "FDAS"], ["asdf", "fdaa"]]

for l in lst:
    print(l)
    for i in l:
        print(i)