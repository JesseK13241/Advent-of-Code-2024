# Each antenna is tuned to a specific frequency indicated by a
# single lowercase letter, uppercase letter, or digit.
#
# In particular, an antinode occurs at any point that is perfectly in line
# with two antennas of the same frequency - but only when one of the antennas
# is twice as far away as the other.
#
# for any pair of antennas with the same frequency, there are two antinodes,
# one on either side of them.
#
# Calculate the impact of the signal.
# How many unique locations within the bounds of the map contain an antinode?

# IDEA:
# for each unique letter:
#   for each unique pair:
#       calculate number of nodes

import itertools
import sys


def get_antinodes(lines: list[str], letter: str, harmonics=False) -> int:
    positions = []
    antinodes = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == letter:
                positions.append((x, y))

    pairs = list(itertools.combinations(positions, 2))
    print(f"\nPairs for letter {letter}: {pairs}")
    for a, b in pairs:
        # 2, 3 --> 1, 2, 3, 4
        counter = 0
        while True:
            missed = 0
            counter += 1
            distance = ((b[0] - a[0]), (b[1] - a[1]))
            distance = (distance[0] * counter, distance[1] * counter)
            # print(f"Distance between {a} and {b} is {distance}")
            location_behind = (a[0] - distance[0], a[1] - distance[1])
            location_front = (b[0] + distance[0], b[1] + distance[1])
            try:
                c, d = location_behind[0], location_behind[1]
                assert 0 <= c < len(lines[0])
                assert 0 <= d < len(lines)
                if lines[d][c] == ".":
                    lines[d][c] = "#"
                else:
                    pass
                antinodes.add(location_behind)

            except (AssertionError, IndexError):
                missed += 1

            try:
                c, d = location_front[0], location_front[1]
                assert 0 <= c <= len(lines[0])
                assert 0 <= d <= len(lines)
                if lines[d][c] == ".":
                    lines[d][c] = "#"
                else:
                    pass
                antinodes.add(location_front)
            except (AssertionError, IndexError):
                missed += 1

            if (not harmonics) or (missed >= 2):
                break

    if harmonics:
        for p in positions:
            antinodes.add(p)
    return antinodes


def first_challenge(lines, harmonics=False):
    unique_letters = set()
    lines = [list(line) for line in lines]
    antinodes = set()
    for line in lines:
        for char in line:
            unique_letters.update(char)

    unique_letters.remove(".")
    print(f"Unique letter: {unique_letters}")

    for letter in unique_letters:
        letter_antinodes = get_antinodes(lines, letter, harmonics)
        print(
            f"Letter {letter} antinodes: {letter_antinodes} ({len(letter_antinodes)})"
        )
        antinodes.update(letter_antinodes)

    for line in lines:
        print(*line)

    print(f"All antinodes: {antinodes} ({len(antinodes)})")
    return len(antinodes)


def second_challenge(lines):
    # After updating your model, it turns out that an antinode occurs at any grid position exactly
    # in line with at least two antennas of the same frequency, regardless of distance.

    return first_challenge(lines, harmonics=True)


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
