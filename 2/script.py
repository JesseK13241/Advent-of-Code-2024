# Report counts as safe if both of the following are true:
# 1) the levels are either all increasing or all decreasing.
# 2) any two adjacent levels differ by at least one and at most three.


def shared_sign(number_list: list[int]) -> bool:
    """Check if a list of nonzero numbers shares the same sign
    >>> shared_sign([1,2,3,4])
    True
    >>> shared_sign([1])
    True
    >>> shared_sign([1, 0])
    False
    >>> shared_sign([-1, -2, -3])
    True
    >>> shared_sign([0, 0, -3])
    False
    >>> shared_sign([0, 0, 0])
    False
    """
    if 0 in number_list:
        return False
    sorted_list = sorted(number_list)
    sign_of_highest = max(sorted_list) > 0
    sign_of_lowest = min(sorted_list) > 0
    return sign_of_highest == sign_of_lowest


def check_if_within_valid_range(number_list: list[int], valid_range=(1, 3)) -> bool:
    """Check if numbers in a list are below a given absolute valid range
    >>> check_if_within_valid_range([1,2,3,4])
    False
    >>> check_if_within_valid_range([1,2,3])
    True
    >>> check_if_within_valid_range([0])
    False
    >>> check_if_within_valid_range([-1,2,-3])
    True
    """
    a, b = valid_range
    for i in range(len(number_list)):
        number = number_list[i]
        if (abs(number) < a) or (abs(number) > b):
            return False
    return True


def calculate_list_safety(number_list: list[int]):
    differences = []
    for i in range(0, len(number_list) - 1):
        difference = number_list[i] - number_list[i + 1]
        differences.append(difference)

    return shared_sign(differences) and check_if_within_valid_range(differences)


def first_challenge(lines):
    total = 0
    for line in lines:
        line = [int(number) for number in line.split()]
        print(f"line: {line}")
        if calculate_list_safety(line):
            total += 1
            print("line is safe\n")
        else:
            print("line is not safe\n")

    return total


def second_challenge(lines):
    # Now, the same rules apply as before, except if removing a single level
    # from an unsafe report would make it safe, the report instead counts as safe.

    # BRUTE FORCE

    total = 0
    for line in lines:
        line = [int(number) for number in line.split()]
        if calculate_list_safety(line):
            total += 1
        else:
            for i in range(len(line)):
                shorter_line = line.copy()
                shorter_line.pop(i)
                if calculate_list_safety(shorter_line):
                    total += 1
                    print(f"full line: {line}")
                    print(f"shorter line: {shorter_line}")
                    print("line is safe")
                    break

    return total


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read().splitlines()
    print(second_challenge(lines))
