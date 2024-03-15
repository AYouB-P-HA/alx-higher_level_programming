#!/usr/bin/python3 
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div 
    import sys 
    i = len(argv)
    if i != 4:
        print('usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
    else:
        a = int(argv[1])
        b = int(args[3])
        operator = args[2]
        if operator == '+':
                print('{} + {} = {}'.format(a, b, add(a, b)))
                exit(0)
        elif operator == '-':
                print('{} - {} = {}'.format(a, b, sub(a, b)))
                exit(0)
        elif operator == '*':
                print('{} * {} = {}'.format(a, b, mul(a, b)))
                exit(0)
        elif operator == '/':
                print('{} / {} = {}'.format(a, b, div(a, b)))
                exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
