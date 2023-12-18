#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    count =  0
    for i in range(x):
        try:
            if isinstance(my_list[i], int):
                print("{:d}\n".format(my_list[i]), end="")
                count += 1
                if count == x:
                    break
        except IndexError:
            print("IndexError: list out of range")
    return count
