print("Welcome to binary search")

count = 0
mn = 0
mx = 100
result = 0

num = int(input("Enter a number between 0 and 100: "))
if num < 0 or num > 100:
    print("Not a valid number. Please try again")
else:
    while num != result:
        result = int((mn + mx) / 2)
        if num > result:
            mn = result
        else:
            mx = result
        count += 1
        print(f"min={mn}\t\tmax={mx}\t\tres={result}")
print(f"It took {count} steps to get to your result {num}")
