import random
words = ["apple", "peach", "tangerine", "dragonfruit"]

print("Your word:", "_" * len(word := random.choice(words)))
guess = ['_'] * len(word)
wrong = 0
done = []

while wrong != 7:
    find = False
    if guess.count("_") == 0:
        print("You got the word!")
        break
    letter = input("Input a letter to guess:")
    while letter in done:
        letter = input("You already guessed this! try again:")
    if letter not in done:
        done.append(letter)
    for i in range(len(word)):
        if word[i] == letter:
            guess[i] = word[i]
            print(guess)
            find = True
    if not find:
        wrong = wrong + 1
        print(f"Letter not in word!, you have {7-wrong} guesses left")

print("you lost!")
