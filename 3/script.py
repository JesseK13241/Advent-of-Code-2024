# Scan the corrupted memory for uncorrupted mul instructions. 
# What do you get if you add up all of the results of the multiplications?
# Sequences like mul(4*, mul(6,9!, ?(12,34), or mul ( 2 , 4 ) do nothing.

def first_challenge(filename):
    total = 0
    for line in lines:
        for part in line.split("mul("):
            numbers = part.split(")")[0]
            try:
                if "," in numbers:
                    a,b = numbers.split(",")
                    a = int(a)
                    b = int(b)
                    total += (a * b)
            except ValueError:
                continue
    return total


def second_challenge(line):
    # The do() instruction enables future mul instructions.
    # The don't() instruction disables future mul instructions.

    total = 0
    enabled = True
    for part in line.split("don't("):
        print(f"\nProcessing part {part}")
        smaller_parts = part.split("do()")
        print(f"All smaller parts: {smaller_parts}")
        for small_part in smaller_parts:
            print(f"  Small part: {small_part}")
            for part in small_part.split("mul("):
                numbers = part.split(")")[0]
                print(f"    Maybe valid mul: {numbers}")
                try:
                    if "," in numbers:
                        a,b = numbers.split(",")
                        a = int(a)
                        b = int(b)
                        if enabled:
                            print(f"      Adding {a*b} to the total")
                            total += (a * b)
                        else:
                            print("      Skipping due to mul being disabled")
                except ValueError:
                    continue
            print("  do() found, enabling mul")
            enabled = True  

        if enabled:
            print("Mul now disabled")
            enabled = False
    return total


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read()
    print(second_challenge(lines))
