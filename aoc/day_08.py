import numpy as np


def part_one(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    directions = list(map(lambda x: int(x == "R"), lines[0].strip()))

    nodes = {line[:3]: (line[7:10], line[12:15]) for line in lines[2:]}

    i = 0
    node = "AAA"
    while node != "ZZZ":
        node = nodes[node][directions[i % len(directions)]]
        i += 1
    return i


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    nodes = {line[:3]: [line[7:10], line[12:15]] for line in lines[2:]}
    directions = list(map(lambda x: int(x == "R"), lines[0].strip()))

    starting_nodes = [node for node in nodes.keys() if node[-1] == "A"]
    lcms = []
    for node in starting_nodes:
        i = 0
        while node[-1] != "Z":
            node = nodes[node][directions[i % len(directions)]]
            i += 1
        lcms.append(i)

    return np.lcm.reduce(lcms)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_08.txt"))
    print(part_two("aoc/inputs/day_08.txt"))
