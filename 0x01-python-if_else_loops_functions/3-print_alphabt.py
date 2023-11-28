#!/usr/bin/python3
i = 0
while i < 26:
    if chr(i + ord('a')) not in ['q', 'e']:
        print("{:s}".format(chr(i + ord('a'))), end="")
    i += 1
