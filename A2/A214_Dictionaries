import re

def count_letter(instring):
    Dict = {}
    done = []

    for i in instring.lower():
        if i not in done:
            Dict[i] = 1
            done.append(i)
        else:
            Dict[i] += 1

    for i in sorted(done):
        print(i, Dict[i])

def count_word():
    all = ""
    with open("alice.txt", "r") as file:
        for line in file:
            line = re.sub(r'[^\w\s]', ' ', line)
            all += line.lower().rstrip().lstrip() + " "
    words = all.split(" ")

    Dict = {}
    done = []

    for i in words:
        if i not in done:
            Dict[i] = 1
            done.append(i)
        else:
            Dict[i] += 1

    del Dict[""]
    done.remove("")

    for i in sorted(done):
        if Dict[i] > 50:
            print(i, Dict[i])

    maxlen = 0
    for i in Dict:
        if len(i) > maxlen:
            maxlen = len(i)
            word = i
    print("Longest word:", word, maxlen)
