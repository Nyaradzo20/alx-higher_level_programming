#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):

    if my_list:
        for index in my_list[::-1]:
            print("{:d}".format(index))
'''
another method
#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    print(*my_list[::-1], sep = "\n")




