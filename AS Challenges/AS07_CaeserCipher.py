def encrypt():
    text = input("Please write out the text you would like to encipher:").lower()
    shift = int(input("What value would you like to shift by?"))
    cipher = ""
    for i in range(len(text)):
        s = ord(text[i]) + shift
        if text[i] == " ":
            cipher = cipher + " "
        elif s > 122:
            t = ((s - 122)//26)+1
            cipher = cipher + chr(s - 26*t)
        else:
            cipher = cipher + chr(ord(text[i]) + shift)
    print(f"Encrypted text: {cipher}")


def decrypt():
    cipher = input("Please write out the text you would like to decipher:").lower()
    shift = int(input("What value would was it shifted by? Write -1 if not known:"))
    text = ""

    if shift != -1:
        for i in range(len(cipher)):
            s = ord(cipher[i]) - shift
            if cipher[i] == " ":
                text = text + " "
            elif s < 97:
                text = text + chr(123 - ((97 - s) % 26))
            else:
                text = text + chr(ord(cipher[i]) - shift)
        print(f"Decrypted text: {text}")
    else:
        print("Printing all possible shifts...")
        shift = 1
        for j in range(1, 26):
            for i in range(len(cipher)):
                s = ord(cipher[i]) - shift
                if cipher[i] == " ":
                    text = text + " "
                elif s < 97:
                    text = text + chr(123 - ((97 - s) % 26))
                else:
                    text = text + chr(ord(cipher[i]) - shift)
            print(f"Shift of {j}: {text}")
            shift = shift + 1
            text = ""


choice = int(input("Would you like to encrypt, or decrypt a message? 1/2"))

if choice == 1:
    encrypt()
elif choice == 2:
    decrypt()
else:
    print("Please choose a valid option.")
