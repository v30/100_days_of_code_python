# Day 2 - Understanding data types

# Welcome message
print("Welcome to the tip calculator.")
totalBill = float(input("What was the total bill? $"))
people = float(input("How many people to split the bill? "))
percentage = float(input("What percentage tip would you like to give? 10, 12, or 15? "))

# Calculate
output = (totalBill + (totalBill*percentage/100))/people
output = f"{output:.2f}"
# Output
print("Each person should pay: $"+str(output))

# Identify the type of var
# print(type(output))

# # 4 primitive data types
# int(123)            # Integer
# str("abc")          # String
# float(123.00)       # Float
# var = True          # Boolean

# # Math operators python
# print(3 + 2)        # +
# print(3 - 2)        # -
# print(3 * 2)        # *
# print(3 / 2)        # /
# print(3**2)         # 3 power of (2) in this case
# print(3%2)          # modulus

# name = input("your name? ")
# for x in range(len(name)):
#     pos = len(name) - x - 1
#     print(name[pos])