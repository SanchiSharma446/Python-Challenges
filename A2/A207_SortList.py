def sortlist(userlist):
    userlist = sorted(userlist)
    print(userlist)
    with open("words.txt", "a") as file:
        for i in userlist:
            file.write(i)
