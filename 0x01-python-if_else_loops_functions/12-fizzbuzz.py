#!/usr/bin/python3
def fizzbuzz():

    for num in range(1, 101):
        if num % 3 == 0:
            if num % 5 == 0:
                print("FizzBuzz ", end='')
            else:
                print("Fizz ", end='')
        elif num % 5 == 0:
            print("Buzz ", end='')
        else:
            print("{:d} ".format(num), end='')