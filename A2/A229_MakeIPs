import random
import string

def make_ipv4():
    for i in range(50):
        IPV4_addresses = []
        IPV4 = ""
        for i in range(4):
            IPV4 += str(random.randint(0,255)) + "."
        IPV4 = IPV4[:-1]
        IPV4_addresses.append(IPV4)

def make_IPV6():
    for i in range(50):
        IPV6_addresses = []
        IPV6 = ""
        for i in range(8):
            part = ''.join(random.choices(string.hexdigits, k=4)).upper()
            if part == "0000":
                IPV6 += "::"
            else:
                IPV6 += part + ":"
        IPV6 = IPV6[:-1]
        IPV6_addresses.append(IPV6)
