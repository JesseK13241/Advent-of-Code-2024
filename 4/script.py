# This word search allows words to be horizontal, vertical, diagonal, written backwards. How many times does XMAS appear?


def find_word(
    lines: list[str], position: tuple[int, int], direction: tuple[int, int], word="XMAS"
) -> bool:
    x, y = position
    dx, dy = direction
    
    try:
        for i in range(1, len(word)):
            new_x = x + dx * i
            new_y = y + dy * i
            assert len(lines) > new_y >= 0
            assert len(lines[0]) > new_x >= 0
            if lines[new_y][new_x] == word[i]:
                if i == len(word) - 1:
                    print(f"Word '{word}' found starting from {position} in direction {direction}")
                    return True
            else:
                break

    except AssertionError:
        return False


def first_challenge(lines):
    # Approach 1:
    # From every X, follow all 8 directions
    words_found = 0
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            if lines[y][x] == "X":
                for dy in [-1, 0, 1]:
                    for dx in [-1, 0, 1]:
                        if (dy == 0) and (dx == 0):
                            continue
                        word_found = find_word(lines, (x, y), (dx, dy))
                        if word_found:
                            words_found += 1

    return words_found


def second_challenge(lines):
    """
    you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

    M.S
    .A.
    M.S
    """
    # For every A, check both diagonals

    target_diagonal = set(("M", "S"))

    words_found = 0
    for y in range(1, len(lines)-1):
        for x in range(1, len(lines[y])-1):
            if lines[y][x] == "A":

                uphill_diagonal = set((lines[y+1][x-1], lines[y-1][x+1]))
                downhill_diagonal = set((lines[y-1][x-1], lines[y+1][x+1]))

                if uphill_diagonal == downhill_diagonal == target_diagonal:
                    print(f"X-MAS found at location (x={x}, y={y})")
                    words_found += 1

    return words_found


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read().splitlines()
    print(second_challenge(lines))
