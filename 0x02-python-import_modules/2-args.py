#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argument = sys.argv[1:]
    i = len(argument)
    if i == 0:
        print('{} arguments.\n'.format(i))
    elif i == 1:
        print('{} argument:\n'.format(i))
        print('{}: {}\n'.format(i, sys.argv[1]))
    else:
        print('{} arguments:\n'.format(i))
        for x in range(1, i+1):
            print('{}: {}\n'.format(x, sys.argv[x]))
