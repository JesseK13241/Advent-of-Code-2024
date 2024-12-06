# What do you get if you add up the middle page number of correctly-ordered updates?

# Approach 1: Generate a sorted list out of ordering rules
# Then, for each input number, get its index in the sorted list
# Then, check if the index list is ascending

# NVM, the ordering rules might not map into a single list: [1..10 & a..z] == [a..z & 1..10]
# --> BRUTE FORCE

# Spaghetti warning


def verify_list(numbers: list[str], rules) -> bool:
    comes_before = {}

    for line in rules:
        # 47|53
        a, b = line.split("|")
        if a in comes_before:
            comes_before[a].append(b)
        else:
            comes_before[a] = [b]

    last_index = len(numbers)
    status = True

    for i in range(last_index):
        num = numbers[i]
        if num in comes_before:
            for x in comes_before[num]:
                try:
                    if numbers.index(num) > numbers.index(x):
                        print(f"Incorrect list {numbers}, {num} should come before {x}")
                        status = False
                        break
                except ValueError:
                    continue

    return status


def first_challenge(pages, rules):
    correct_pages = []

    for page in pages:
        page = page.split(",")
        if verify_list(page, rules):
            correct_pages.append(page)

    print()
    total = 0
    for page in correct_pages:
        mid = int(page[len(page) // 2])
        total += mid

    return total


def filter_rules(rules, numbers: list[str]):
    r = {number: {"a": [], "b": []} for number in numbers}
    # rules = {'47': {'b': ['53', '13', '61', '29'], 'a': ['97', '75']},  ...}

    for rule in rules:
        if rule in numbers:
            if "a" in rules[rule]:
                for number in rules[rule]["a"]:
                    if number in numbers:
                        r[rule]["a"].append(number)
            if "b" in rules[rule]:
                for number in rules[rule]["b"]:
                    if number in numbers:
                        r[rule]["b"].append(number)

    return r


def generate_rule_structure(rules):
    r = {}

    for rule in rules:
        a, b = rule.split("|")
        if a in r:
            if "b" in r[a]:
                r[a]["b"].append(b)
            else:
                r[a]["b"] = [b]
        else:
            r[a] = {"b": [b]}

        if b in r:
            if "a" in r[b]:
                r[b]["a"].append(a)
            else:
                r[b]["a"] = [a]
        else:
            r[b] = {"a": [a]}

    return r


def fix_page(numbers: list[str], rules):
    print(f"Fixing numbers {numbers}")

    from_start = []
    from_end = []

    filtered = filter_rules(rules, numbers)

    while True:
        first_item = []
        last_item = []

        for rule in filtered:
            # print(f"Rules for {rule}")
            if not filtered[rule]["a"]:
                last_item.append(rule)
            elif not filtered[rule]["b"]:
                first_item.append(rule)

        # print(f"First: {first_item}")
        # print(f"Last: {last_item}")

        assert len(first_item) == 1
        assert len(last_item) == 1

        numbers.remove(first_item[0])
        numbers.remove(last_item[0])

        from_start.append(first_item[0])
        from_end.append(last_item[0])

        if len(numbers) == 1:
            fixed = from_start + numbers + from_end
            print(fixed)
            return fixed

        filtered = filter_rules(filtered, numbers)


def second_challenge(pages, rules):
    # Find the updates which are not in the correct order.
    # What do you get if you add up the middle page numbers
    # after correctly ordering just those updates?

    # Challenge suggests that there exists only one correct ordering after all

    fixed_pages = []

    print(f"Rules: {rules}")
    structured_rules = generate_rule_structure(rules)
    print(f"Rules (structured): {structured_rules}")

    for page in pages:
        print(f"Processing page {page}")
        page = page.split(",")
        if verify_list(page, rules):
            continue
        fixed_page = fix_page(page, structured_rules)
        if fixed_page:
            fixed_pages.append(fixed_page)

    total = 0
    for page in fixed_pages:
        mid = int(page[len(page) // 2])
        total += mid

    return total


if __name__ == "__main__":
    with open("input") as f:
        lines = f.read().splitlines()
        separator_index = lines.index("")

        rules = lines[:separator_index]
        print(f"{len(rules)} ordering rules")

        pages = lines[separator_index + 1 :]
        print(f"{len(pages)} pages\n")

        print(second_challenge(pages, rules))
