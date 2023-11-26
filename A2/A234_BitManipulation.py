def OR(a, b):
    num = ""
    for i in range(len(a)):
        num += str(int(a[i]) + int(b[i]))
    print(num)


def AND(a, b):
    num = ""
    for i in range(len(a)):
        num += str(int(a[i]) * int(b[i]))
    print(num)


def NOT(a):
    num = ""
    for i in range(len(a)):
        if a[i] == "1":
            num += "0"
        else:
            num += "1"
    print(num)


def XOR(a, b):
    num = ""
    for i in range(len(a)):
        if a[i] == b[i]:
            num += "0"
        else:
            num += "1"
    print(num)


binary = input("Please input your binary number: ")

check = True

while True:
    count = 0
    for i in binary:
        if i in ["0", "1"]:
            check = True
        else:
            check = False
    if check == False:
        binary = input("Please input a valid binary number: ")
    else:
        break

if choice := input("What operation would you like to do? OR, AND, XOR, NOR") == 'OR':
    mask = input("Please input your mask: ")
    OR(binary, mask)
elif choice == 'AND':
    mask = input("Please input your mask: ")
    AND(binary, mask)
elif choice == 'XOR':
    mask = input("Please input your mask: ")
    XOR(binary, mask)
elif choice == 'NOT':
    NOT(binary)
else:
    print("Not valid operation")
