def card_winnings(line: str):

    line = line[line.index(":") + 2 :].strip()

    winning_card, your_card = line.split("|")

    winning_card = set(
        int(x.strip()) for x in winning_card.strip().split(" ") if x.strip() != ""
    )
    your_card = set(
        int(x.strip()) for x in your_card.strip().split(" ") if x.strip() != ""
    )

    return len(winning_card.intersection(your_card))


def power_two_winnings(line: str):

    n_winnings = card_winnings(line)
    if n_winnings > 0:
        return 2 ** (n_winnings - 1)
    else:
        return 0


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

    return sum(map(power_two_winnings, lines))


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    scratch_card_counts = {i: 1 for i in range(len(lines))}

    for i in range(len(lines)):
        n_cards = card_winnings(lines[i])
        for j in range(i + 1, i + 1 + n_cards):
            scratch_card_counts[j] += scratch_card_counts[i]

    return sum(scratch_card_counts.values())


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_04.txt"))
    print(part_two("aoc/inputs/day_04.txt"))
