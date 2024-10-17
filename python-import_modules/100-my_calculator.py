#!/usr/bin/python3
from calculator_1 import *
import sys
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)

    if args[2] not in ["+", "-", "*", "/"]:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(args[1])
    b = int(args[3])

    if args[2] == "+":
        result = add(a, b)
    elif args[2] == "-":
        result = sub(a, b)
    elif args[2] == "*":
        result = mul(a, b)
    elif args[2] == "/":
        result = div(a, b)

    print("{} {} {} = {}".format(args[1], args[2], args[3], args[result]))
