#!/usr/bin/python3
for numb in range(0, 9):
    for comb in range(numb + 1, 10):
        if numb == 8:
            print("{}{}".format(numb, comb))
        else:
            print("{}{}".format(numb, comb), end=", ")
