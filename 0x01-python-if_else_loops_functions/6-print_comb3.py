#!/usr/bin/python3
comma = ", "
for i in range(10):
    for j in range(10):
        if (i < j):
            print("{}{}".format(i, j), end="")
            if (i != 8 or (i == 8 and j != 9)):
                print(comma, end="")
