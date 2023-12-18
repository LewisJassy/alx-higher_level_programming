#!/usr/bin/python3

def safe_print_integer(value):
    while(value):
        try:
            if isinstance(value, int):
                print("{:d}".format(value))
                return True
            else:
                return False
        except ValueError:
            break
    print()
    return value
