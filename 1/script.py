# What is the total distance between lists?

def first(filename):
    with open(filename) as f:
        lines = f.read().splitlines()
    
    first_column = []
    second_column = []

    for line in lines:
        if line:
            a, b = line.split()
            first_column.append(a)
            second_column.append(b)

    total_distance = 0

    for a, b in zip(sorted(first_column), sorted(second_column)):
        distance = abs(int(a) - int(b))
        total_distance += distance

    return total_distance

def second(filename):
    # Calculate a total similarity score by adding up each number in the left list after 
    # multiplying it by the number of times that number appears in the right list.

    with open(filename) as f:
        lines = f.read().splitlines()
    
    first_column = []
    second_column = []

    for line in lines:
        if line:
            a, b = line.split()
            first_column.append(a)
            second_column.append(b)

    total_similarity = 0

    for a in first_column:
        similarity = int(a) * second_column.count(a)
        total_similarity += similarity

    return total_similarity

if __name__ == "__main__":
    print(second("input"))
