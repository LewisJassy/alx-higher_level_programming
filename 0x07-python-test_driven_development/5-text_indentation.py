#!/usr/bin/python3


def text_indentation(text):
    """prints a char followed by newline 
    if encounter '.', '?' and ':'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in text:
        print(char, end="")
        if char == "." or char == ":" or char == "?":
            print("\n")
