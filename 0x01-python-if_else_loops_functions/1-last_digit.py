#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last_int = number % -10
else:
    last_int = number % 10
if last_int > 5:
    print("Last digit of {:d} is {:d} and is greater than 5"
          .format(number, last_int))
elif last_int < 6 and last_int != 0:
    print("Last digit of {:d} is {:d} and is less than 6 and not 0"
          .format(number, last_int))
else:
    print("Last digit of {:d} is {:d} and is 0".format(number, last_int))
