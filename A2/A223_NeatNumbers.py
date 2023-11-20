count = 0
neat_nums = []

for i in range(101,1000):
    sum = 0
    for j in str(i):
        sum += int(j)
    if i%sum == 0:
        count += 1
        neat_nums.append(i)

print(neat_nums, count)
