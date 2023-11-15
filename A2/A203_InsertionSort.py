from random import randint

array = [randint(1, 100) for x in range(9)]

for i in range(1, len(array)):
    val = array[i]

    while array[i - 1] > val and i > 0:
        temp = array[i]
        array[i] = array[i - 1]
        array[i - 1] = temp
        i = i - 1

print(array)
