#!/usr/bin/python3
def uppercase(str):
    nstr = ""
    for i in range(len(str)):
        if (ord(str[i]) >= 97 and ord(str[i]) <= 122):
            nstr += chr(ord(str[i]) - 32)
            continue
        nstr += str[i]
    print("{}".format(nstr))
