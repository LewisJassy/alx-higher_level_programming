#!/usr/bin/python3

def say_my_name(first_name, last_name=""):
    if first_name != str(first_name):
        raise TypeError("first_name must be a string")
    if last_name != str(last_name):
        raise TypeError("last_name must be a string")
    if first_name == "" and last_name == "":
        raise ValueError("String is empty")
    return first_name, last_name