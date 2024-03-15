#!/usr/bin/python3 
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div 
    import sys 
    args = sys.argv[1:]
    i = len(args)
    if i != 3:
        print('usage: ./100-my_calculator.py <a> <operator> <b>')
        sys.exit(1)
    else:
        a = int(args[0])
        b = int(args[2])
        operator = args[1]
        match operator:
            case '+':
                print('{} + {} = {}'.format(a, b, add(a, b)))
            case '-':
                print('{} - {} = {}'.format(a, b, sub(a, b)))
            case '*':
                print('{} * {} = {}'.format(a, b, mul(a, b)))
            case '/':
                print('{} / {} = {}'.format(a, b, div(a, b)))
            case _:
                print('Unknown operator. Available operators: +, -, * and /')
                sys.exit(1)
