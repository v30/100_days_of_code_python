# Get a random name from a list of names
import random
print("Welcome to Random name from List")

list_of_names = ["Owen", "Danielle", "Caitlyn", "Tyler", "Riley"]

list_item = random.randint(0, len(list_of_names) - 1)

print(list_of_names[list_item])
