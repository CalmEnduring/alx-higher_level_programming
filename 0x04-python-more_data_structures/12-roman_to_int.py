#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or type(roman_string) is not str:
        return None

    romlet = [
        ["M", 1000], ["D", 500], ["C", 100], ["L", 50],
        ["X", 10], ["V", 5], ["I", 1]
    ]

    number = 0
    last_num = 0
    
    for let in roman_string:
        for el in romlet:
            if let == el[0]:
                if last_num == 0 or last_num >= el[1]:
                    number += el[1]
                elif last_num < el[1]:
                    number += el[1] - (last_num * 2)

                last_num = el[1]
    return number
