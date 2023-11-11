inputs = []

with open("inputs.txt", 'r') as file:
    for line in file:
        inputs.append(line.rstrip())

lights = ["."] * int(inputs[0])


for i in range(len(inputs)):
    inputs[i] = inputs[i].split(" ")

for i in range(1, len(inputs)):
    if (a := int(inputs[i][0])) > (b := int(inputs[i][1])):
        b = int(inputs[i][0])
        a = int(inputs[i][1])
    for j in range(a, b+1):
        if lights[j] == "X":
            lights[j] = "."
        elif lights[j] == ".":
            lights[j] = "X"
    print(lights)
count = 0
for i in lights:
    if i == "X":
        count += 1

print(count)
