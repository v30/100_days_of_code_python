# Welcome
# This is a true love calculator. Using a well known algorithm to calculate the score.
# Use the letters in TRUE LOVE and calculate how many times a letter appears, add the score of true and the score of love
# Example Jack and Jill
# T = 0, R = 0, U = 0, E = 0: 0         and L = 2, O = 0, V = 0, E = 0: 2       concat 0 and 2 for a total of 2%
name1 = input()
name2 = input()

combined_names = name1.lower() + name2.lower()
test = ["true", "love"]
total = ""

for word in test:
    count = 0
    for l in word:
        count += combined_names.count(l)
    total += str(count)

print(f"Your love score is: {total}%")
