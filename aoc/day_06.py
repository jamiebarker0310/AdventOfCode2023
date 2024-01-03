import math


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

    times = map(int, filter(lambda x: len(x) > 0, lines[0].strip().split(" ")[1:]))
    distances = map(int, filter(lambda x: len(x) > 0, lines[1].strip().split(" ")[1:]))
    prod = 1
    for t, d in zip(times, distances):
        xmax = (t + (t ** 2 - 4 * d) ** 0.5) / 2
        xmin = (t - (t ** 2 - 4 * d) ** 0.5) / 2
        n_sols = 1 + math.floor(xmax - 1e-7) - math.ceil(xmin + 1e-7)
        prod *= n_sols
    return prod


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    t = int("".join(filter(lambda x: len(x) > 0, lines[0].strip().split(" ")[1:])))
    d = int("".join(filter(lambda x: len(x) > 0, lines[1].strip().split(" ")[1:])))
    xmax = (t + (t ** 2 - 4 * d) ** 0.5) / 2
    xmin = (t - (t ** 2 - 4 * d) ** 0.5) / 2
    n_sols = 1 + math.floor(xmax - 1e-7) - math.ceil(xmin + 1e-7)
    return n_sols


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_06.txt"))
    print(part_two("aoc/inputs/day_06.txt"))
