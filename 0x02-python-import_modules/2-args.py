#!/usr/bin/python3
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))

    for i in range(len(sys.argv)):
        if i == 0:
            continue
        print("{}: {}".format(i, sys.argv[i]))