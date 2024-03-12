#!/usr/bin/python3
import random
number = -55540
if number >= 0:
    last_digit = str(number)[-1]
else:
    last_digit = str(number)[0] + str(number)[-1]
if last_digit > '5' and number > 0:
    print(f'Last digit of {number} is {last_digit} and is greater than 5')
elif last_digit == '0':
    print(f'Last digit of {number} is {last_digit} and is 0')
else:
    print(f'Last digit of {number} is {last_digit} and is less than 6 and not 0')
