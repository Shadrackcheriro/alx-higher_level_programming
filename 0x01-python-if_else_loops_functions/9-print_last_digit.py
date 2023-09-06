#!/usr/bin/python3
def print_last_digit(number):
    lastDigit = str(number)[-1]
    lastDigit = int(lastDigit)
    print(f"{lastDigit:d}", end="")
    return (lastDigit)
