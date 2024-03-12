#!/usr/bin/python3
def uppercase(s):
    result = ''
    for x in range(0, len(s)):
        char = s[x]
        i = ord(char)
        if i >= 97 and i < 123:
            j = i - 32
            result += chr(j)
        else:
            result += char
    return print('{}'.format(result), end=" \n")
