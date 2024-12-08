# Each line represents a single equation.
# Operators are always evaluated left-to-right.
# Two different types of operators:
#   add (+) and multiply (*).
# Determine which equations could possibly be true.
# What is their total calibration result?

import sys
from itertools import product


def first_challenge(lines):
    # 292: 11 6 16 20
    operators = "*+"
    correct_totals = 0
    for line in lines:
        total, numbers = line.split(": ")
        total = int(total)
        count = len(numbers.split()) - 1
        numbers = numbers.replace(" ", ")_")
        numbers = numbers.replace(")", "", 1)
        numbers = ("(" * count) + numbers + ")"
        # (((11_6)_16)_20)

        op_combinations = list(product(operators, repeat=count))
        for op_combination in op_combinations:
            test = numbers
            for op in op_combination:
                test = test.replace("_", op, 1)

            result = eval(test)
            if result == total:
                print(f"{test} = {total}")
                correct_totals += result
                break

    return correct_totals


def _add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def combine(a, b):
    return int(str(a) + str(b))


def process_with_op(queue: list[int], total: int, op = None):
    # print(f"Processing line {queue} with {op}")

    if op:
        if len(queue) == 1:
            if queue[0] == total:
                return total
            return

        a = queue.pop()
        b = queue.pop()

        if a > total or b > total:
            # print("Too high, breaking")
            return

        queue.append(op(a, b))

    a = process_with_op(queue.copy(), total, _add)
    if a:
        return a
    b = process_with_op(queue.copy(), total, multiply)
    if b:
        return b
    c = process_with_op(queue.copy(), total, combine)
    if c:
        return c

def second_challenge(lines):
    correct_totals = 0
    for line in lines:
        total, queue = line.split(": ")
        total = int(total)

        queue = [int(n) for n in queue.split()]
        queue = queue[::-1]  # reversed

        result = process_with_op(queue, total)
        if result:
            prev_total = total
            correct_totals += result
            print(f"{prev_total} + {result} = {total}")

    return correct_totals


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
