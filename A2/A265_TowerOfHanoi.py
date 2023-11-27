def TOH(n, source, dest, aux):
    if n == 1:
        print(f"Disk 1: {source} --> {dest}")
        return
    TOH(n - 1, source, aux, dest)
    print(f"Disk {n}: {source} --> {dest} ")
    TOH(n - 1, aux, dest, source)


n = int(input("How many blocks are on the stack?"))
TOH(n, 'A', 'B', 'C')
