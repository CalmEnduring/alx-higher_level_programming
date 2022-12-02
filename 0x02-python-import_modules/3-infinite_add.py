#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    
    sa = argv
    larg = len(sa)
    sum = 0

    if larg > 1:
        for i in range(1, larg):
            sum += int(sa[i])

    print(sum)
