#!/usr/bin/python3
def print_list_integer(my_list=[]):
    x = len(my_list)
    print('{}'.format(my_list[0]))
    for i in my_list[:x-1]:
        print('{}'.format(my_list[i]))
