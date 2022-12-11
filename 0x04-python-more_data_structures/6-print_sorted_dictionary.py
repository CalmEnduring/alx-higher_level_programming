#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorteddict = sorted(a_dictionary.items())

    for k, v in sorteddict:
        print(f"{k}: {v}")
