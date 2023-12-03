import random

array = random.sample(range(1, 100), 50)

find = int(input("What number between 1 - 50 do you wish to find?"))
found = 0

for i in range(49):
    if find == array[i]:
        print(f"Your number was found at the index of {i}.")
        found = -1
        break

if found != -1:
    print("Your number was not in the array.")
