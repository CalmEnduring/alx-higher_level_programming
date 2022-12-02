#!/usr/bin/python3
import sys
if __name__ == "__main__":
    sa = sys.argv 
    larg = len(sa) - 1 # argument count excluding 1st argument
    # if length of argv > 1
    if larg > 1:
        print(larg, "arguments:") # length of argv + arguments
        for i in range(1, larg + 1): # iterate through each argument - 1st
            print("{}: {}".format(i, sa[i]))
    elif larg == 1: # if argv is 1 (no arguments besides file itself)
        print(larg, "arguments:") # same as 1st if condition
        for i in range(1, larg + 1): # same as 1st for loop
            print("{}: {}".format(i, sa[i]))
    elif larg == 0: # if there are no arguments
        print(larg, "arguments.")
