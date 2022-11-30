#!/usr/bin/python3
def fizzbuzz():
    a = range(1, 101)
    for i in a:
        if ((i % 3 == 0) and (i % 5 == 0)):
            print("FizzBuzz", end=" ")
        elif (i % 3 == 0):
            print("Fizz", end=" ")
        elif (i % 5 == 0):
            print("Buzz", end=" ")
        else:
            print(i, end=" ")
