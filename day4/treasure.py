# Make a treasure map with rows and cols

#       A   B   C   D
#   1
#   2
#   3
#   4           X

# X marks the spot
col = ["a", "b", "c", "d"]
line1 = ["0", "0", "0", "0"]
line2 = ["0", "0", "0", "0"]
line3 = ["0", "0", "0", "0"]
line4 = ["0", "0", "0", "0"]

map = [line1, line2, line3, line4]

pos = input("Where do you want to place the treasure? ")
letter = pos[0].lower()
letter_index = col.index(letter)
number_index = int(pos[1]) - 1
map[number_index][letter_index] = "X"

print(f"{line1}\n{line2}\n{line3}\n{line4}")
