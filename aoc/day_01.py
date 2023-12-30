def calc_exterior_digit(line: str) -> int:

    line = list(filter(lambda x: x.isnumeric(), line))

    return int(line[0] + line[-1])


def calc_exterior_digit_written(line: str) -> int:

    nums = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    nums.update({str(i): str(i) for i in range(1, 10)})

    min_index_dict = {n: line.index(n) for n in nums.keys() if n in line}

    max_index_dict = {n: line.rindex(n) for n in nums.keys() if n in line}

    min_index = nums[min(min_index_dict, key=min_index_dict.get)]

    max_index = nums[max(max_index_dict, key=max_index_dict.get)]

    return int(min_index + max_index)


def part_one(file_path: str) -> int:
    """
    for each line gets the first and last digit and combines them

    Args:
        file_path (str): filepath

    Returns:
        int:
    """

    # read file
    with open(file_path) as f:
        lines = f.readlines()

    return sum(map(calc_exterior_digit, lines))


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return sum(map(calc_exterior_digit_written, lines))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_01.txt"))
    print(part_two("aoc/inputs/day_01.txt"))
