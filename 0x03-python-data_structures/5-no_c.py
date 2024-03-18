#!/usr/bin/python3

def no_c(my_string):
    x = list (my_string.strip())
    result = []
    for char in x: 
        if char != 'c' and char != 'C':
            result.append(char)
    return ''.join(result)
