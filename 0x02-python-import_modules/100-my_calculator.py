#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add, sub, mul, div
    import sys

    argc = len(sys.argv)
    if argc != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    operators = ['+', '-', '*', '/']
    operator = sys.argv[2]
    if operator not in operators:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(sys.argv[1])
    b = int(sys.argv[3])

    print("{} {} {} = ".format(a, operator, b), end="")

    if operator == '+':
        print("{}".format(add(a, b)))
    elif operator == '-':
        print("{}".format(sub(a, b)))
    elif operator == '*':
        print("{}".format(mul(a, b)))
    else:
        print("{}".format(div(a, b)))
