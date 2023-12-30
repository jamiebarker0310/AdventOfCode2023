from functools import reduce


MAX_DICT = {"red": 12, "green": 13, "blue": 14}


def parse_game(line: str) -> int:

    game_id = int(
        "".join([char for char in line[: line.index(":")] if char.isnumeric()])
    )

    games = line[line.index(":") + 2 :].split("; ")

    for game in games:
        for cube in game.split(", "):
            number, color = cube.split(" ")
            if MAX_DICT[color.strip()] < int(number):
                return 0
    return game_id


def parse_game_2(line: str) -> int:

    games = line[line.index(":") + 2 :].split("; ")

    game_data = {"blue": 0, "red": 0, "green": 0}

    for game in games:
        for cube in game.split(", "):
            number, color = cube.split(" ")
            color = color.strip()
            game_data[color] = max(int(number), game_data[color])

    return reduce((lambda x, y: x * y), game_data.values())


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

    return sum(map(parse_game, lines))


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return sum(map(parse_game_2, lines))


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_02.txt"))
    print(part_two("aoc/inputs/day_02.txt"))
