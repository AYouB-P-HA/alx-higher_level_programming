#!/usr/bin/python3
if __name__ == '__main__':
    import sys
    args = sys.argv[1:]
    i = len(args)
    if i == 0:
        print('{}'.format(i))
    else:
        result = 0
        for x in range(1, i+1):
            num = int(sys.argv[x])
            result += num
        print('{}'.format(result))
