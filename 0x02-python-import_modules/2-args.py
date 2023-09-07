#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    x = len(sys.argv) - 1
    if not x:
        print("{} arguments.".format(x))
    elif x == 1:
        print("{} argument:".format(x))
        print("{}: {}".format(x, sys.argv[x]))
    else:
        print("{} arguments:".format(x))
        x = 0
        for arg in sys.argv:
            if x != 0:
                print("{}: {}".format(x, sys.argv[x]))
            x += 1
