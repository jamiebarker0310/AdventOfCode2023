import numpy as np


def adjust_indices(symbol_grid: np.array, i=None, j=None):

    if i is not None:
        if i < 0:
            return 0
        if i >= symbol_grid.shape[0]:
            return symbol_grid.shape[0]
        else:
            return i

    if j is not None:
        if j < 0:
            return 0
        if j >= symbol_grid.shape[1]:
            return symbol_grid.shape[1]
        else:
            return j

    else:
        raise ValueError("Both i and j cannot be None")


def get_number_locations(line: str, i: int, symbol_grid: np.array):

    total = 0

    j = 0
    number = ""
    indices = []

    for j in range(len(line)):
        if line[j].isnumeric():
            number += line[j]
            indices.append((i, j))

        elif number != "":
            _, min_j = min(indices)
            _, max_j = max(indices)

            min_i = adjust_indices(symbol_grid, i=i - 1)
            max_i = adjust_indices(symbol_grid, i=i + 2)
            min_j = adjust_indices(symbol_grid, j=min_j - 1)
            max_j = adjust_indices(symbol_grid, j=max_j + 2)

            if symbol_grid[min_i:max_i, min_j:max_j].sum() > 0:
                total += int(number)

            indices = []
            number = ""

    return total


def get_symbol_locations(line: str):

    line = line.strip()

    line_np = np.zeros(len(line))

    for i in range(len(line)):
        if not (line[i].isnumeric() or line[i] == "."):
            line_np[i] = 1

    return line_np


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

    symbol_grid = np.vstack([get_symbol_locations(line) for line in lines])

    return sum(
        [get_number_locations(line, i, symbol_grid) for i, line in enumerate(lines)]
    )


def get_star_adjacent_numbers(line: str, i: int, star_grid: dict):

    j = 0
    number = ""
    indices = []

    for j in range(len(line)):
        if line[j].isnumeric():
            number += line[j]
            indices.append((i, j))

        elif number != "":
            _, min_j = min(indices)
            _, max_j = max(indices)

            for star_i, star_j in star_grid.keys():
                if star_i >= i - 1 and star_i <= i + 1:
                    if star_j >= min_j - 1 and star_j <= max_j + 1:
                        star_grid[(star_i, star_j)].append(int(number))

            indices = []
            number = ""

    return star_grid


def get_gear_ratio_locations(line: str):

    line = line.strip()

    line_np = np.zeros(len(line))

    for i in range(len(line)):
        if line[i] == "*":
            line_np[i] = 1

    return line_np


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    symbol_grid = np.vstack([get_gear_ratio_locations(line) for line in lines])

    star_grid = {(i, j): [] for i, j in np.argwhere(symbol_grid > 0)}

    for i, line in enumerate(lines):
        star_grid = get_star_adjacent_numbers(line, i, star_grid)

    return sum([val[0] * val[1] for val in star_grid.values() if len(val) == 2])


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_03.txt"))
    print(part_two("aoc/inputs/day_03.txt"))
