words = []
tri_nums = []
count = 0

with open("words.txt", 'r') as file:
    for line in file:
        words = line.split(",")

for n in range(1,100):
    tri_nums.append(0.5*n*(n+1))

for i in words:
    word = i
    sum = 0
    for j in range(1, len(word)-1):
        sum += ord(word[j]) - 65
    if sum in tri_nums:
        count += 1

print(count)
