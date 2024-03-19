#!/usr/bin/python3
def max_integer(my_list=[]):
    x = len(my_list)
    if x == 0:
        return 0
    else:
        for i in range(x-1,0,-1):
            a = my_list[i]
            b = my_list[i-1]
            if a > b:
                my_list.pop(i-1)
            else:
                my_list.pop(i)
        return my_list[0]
