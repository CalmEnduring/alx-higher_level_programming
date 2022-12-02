#!/usr/bin/python3
import sys
if __name__ == "__main__":
    
    sa = sys.argv
    larg = len(sa)
    sum = 0

    if larg > 1:
        for i in range(1, larg):
            sum += int(sa[i])

    print(sum)
