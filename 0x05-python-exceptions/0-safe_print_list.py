#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
""" a function that prints x elements of a list """
    i = nej = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end="")
            nej += 1
        except:
            continue
    print()
    return nej
