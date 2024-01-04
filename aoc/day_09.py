def predict_next(line: str, reverse=False):

    y = list(map(int, line.strip().split(" ")))
    if reverse:
        y = y[::-1]
    final_element = get_difference(y)
    return final_element


def get_difference(y):

    y_diff = [b - a for a, b in zip(y[:-1], y[1:])]
    if sum(y_diff) == 0:
        return y[-1]
    else:
        return y[-1] + get_difference(y_diff)


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

    return sum(map(predict_next, lines))


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return sum(map(lambda x: predict_next(x, reverse=True), lines))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_09.txt"))
    print(part_two("aoc/inputs/day_09.txt"))
