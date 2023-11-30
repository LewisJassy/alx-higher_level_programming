#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    # Count the number of command-line arguments
    nargs = len(sys.argv) - 1
    # Print information about the number of arguments
    print("{:d} {:s}{:s}".format(nargs, "argument" if nargs <= 1 else "arguments",v"." if nargs == 0 else ":"))
    # Iterate through command-line arguments and print them
    for i, arg in enumerate(sys.argv[1:]):
        print("{:d}: {:s}".format(i + 1, arg))
