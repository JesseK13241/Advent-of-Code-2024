#

import sys


def first_challenge(lines):
    for line in lines:
        pass

    return 0


def second_challenge(lines):
    for line in lines:
        pass

    return 0


if __name__ == "__main__":
    # usage:
    # > script
    # > script 1
    # > script 2
    # > script 1 example
    # > script 2 example
    # > script 1 input
    # > script 2 input
    # > script input
    # > script example

    input_file = "example"
    num = 1

    if len(sys.argv) == 2:
        _, param = sys.argv
        if param.isnumeric():
            num = param
        else:
            input_file = param

    if len(sys.argv) == 3:
        _, num, input_file = sys.argv

    with open(input_file) as f:
        lines = f.read().splitlines()

    if int(num) == 2:
        print(second_challenge(lines))
    else:
        print(first_challenge(lines))
