from itertools import permutations


def find_anagrams(input_str):
    return [''.join(perm) for perm in set(permutations(input_str))]


words = []

with open("words.txt", "r") as file:
    for line in file:
        words.append(line.rstrip())

perms = find_anagrams(input("Input your string"))

print(list(set(words) & set(perms)))
