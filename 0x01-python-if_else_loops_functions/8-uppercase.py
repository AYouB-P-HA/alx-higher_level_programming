#!/usr/bin/python3
def uppercase(s):
    for x in range(0, len(s)):
        char = s[x]
        i = ord(char)
        if i >= 97 and i < 123:
            j = i - 32
            print('{}'.format(chr(j)), end=" ")
        else:
            print('{}'.format(char), end=" ")
