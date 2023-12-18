#!/usr/bin/python3

def safe_print_integer(value):
    for i in value:
        try:
            if i == int:
                print("{:d}".format(i))
                return True
            else:
                return False
        except ValueError:
            break
    return value
