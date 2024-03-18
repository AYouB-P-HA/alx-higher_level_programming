<<<<<<< HEAD

def new_in_list(my_list, idx, element): 
    x = my_list.copy()
=======
#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    new_list = my_list[:]
>>>>>>> adfe219dd5e2cc0d9ee2306630241b271df28ae9
    if idx < 0 or idx > (len(my_list) - 1):
        return new_list
    else:
        new_list[idx] = element
        return new_list
