#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    j = 0
    for i in range(x):
        try:
            if type(my_list[i]) is int and j != x:
                print("{:d}".format(my_list[i]), end="")
                j += 1
        except TypeError:
            continue
    print()
    return (j)
