# If there is something directly in front of you, turn right 90 degrees.
# Otherwise, take a step forward.

# How many distinct positions will the guard visit before leaving the mapped area?

import sys

# ....#.....
# .#..^.....
# ........#.

GUARD = ["^", ">", "v", "<"]
PATH = "X"
BARRIER = "#"


def get_initial_position(lines, guard=GUARD[0]):
    for y in range(len(lines)):
        for x in range(len(lines[y])):
            char = lines[y][x]
            if char == guard:
                return (x, y)

    raise "No initial position found"


def count_path_tiles(lines, path=PATH):
    total = 0
    for line in lines:
        total += line.count("X")
    return total


def game_step(lines, position, path=PATH, barrier=BARRIER, past_barriers=set()):
    # 1) Get current direction
    # 2) Replace position with path
    # 3) If barrier on front:
    #       - Rotate 90 degrees
    # 4) Move forwards
    x, y = position
    direction = GUARD.index(lines[y][x])
    lines[y][x] = path

    direction_mapping = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    new_y_d, new_x_d = direction_mapping[direction]
    new_y = y + new_y_d
    new_x = x + new_x_d

    if not ((0 <= new_y < len(lines)) and (0 <= new_x < len(lines[0]))):
        lines[y][x] = path
        return (lines, ((-1, -1)), False)

    if lines[new_y][new_x] == barrier:
        direction = (direction + 1) % len(GUARD)
        new_y_d, new_x_d = direction_mapping[direction]
        new_y = y + new_y_d
        new_x = x + new_x_d

        if lines[new_y][new_x] == barrier:
            # Barrier on the turning direction as well
            direction = (direction + 1) % len(GUARD)
            new_y_d, new_x_d = direction_mapping[direction]
            new_y = y + new_y_d
            new_x = x + new_x_d

        past_barrier = tuple([direction, new_x, new_y])
        if past_barrier in past_barriers:
            return (lines, (-1, -1), True)

        past_barriers.add(past_barrier)

    lines[new_y][new_x] = GUARD[direction]
    return (lines, ((new_x, new_y)), False)


def first_challenge(lines):
    game_state = [list(line) for line in lines]
    position = get_initial_position(lines)
    print(f"Initial position at {position}")
    step = 1

    while True:
        print(f"Game step {step} ----------------------------- ")
        game_state, position, _ = game_step(game_state, position)
        step += 1
        if position == (-1, -1):
            break

    return count_path_tiles(game_state)


def second_challenge(lines):
    # You need to get the guard stuck in a loop by adding a single new obstruction. How many different positions could you choose for this obstruction?

    # IDEA:
    # Calculate path from part 1
    # For each path block, try placing a barrier
    # Track previous 4 barrier coordinates
    # If it doesn't change --> infinite loop

    game_state = [list(line) for line in lines]
    initial_position = get_initial_position(lines)
    position = initial_position
    print(f"Initial position at {position}")

    while True:
        game_state, position, infinite = game_step(game_state, position)
        if position == (-1, -1):
            if infinite:
                print("First game ended in infinite loop")
            else:
                print("First game ended properly")
            break

    positions_to_alter = []
    for y in range(len(game_state)):
        for x in range(len(game_state[0])):
            if game_state[y][x] == PATH:
                if (x, y) != initial_position:
                    positions_to_alter.append((x, y))

    infinite_games = 0

    print(f"{len(positions_to_alter)} barrier positions to try")

    for alter_position in positions_to_alter:
        alter_x, alter_y = alter_position
        game_state = [list(line) for line in lines.copy()]
        position = initial_position
        game_state[alter_y][alter_x] = BARRIER
        past_barriers = set()
        print(f"Barrier at {alter_position}\n")

        while True:
            game_state, position, infinite = game_step(
                game_state,
                position,
                past_barriers=past_barriers,
            )

            if position == (-1, -1):
                if infinite:
                    print(f"Game {alter_position} ended in infinite loop")
                    # game_state[alter_y][alter_x] = "O"
                    # print("\nInfinite: ")
                    # for line in game_state:
                    #    print(*line)
                    infinite_games += 1
                else:
                    # print(f"Game {alter_position} ended properly")
                    pass
                break

    return infinite_games


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
