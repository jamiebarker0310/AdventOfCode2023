from collections import Counter


def parse_hand(hand, joker=False):

    hand_counter = Counter(hand)
    if joker:
        joker_count = hand_counter[1]
        hand_counter_len = len(hand_counter)
        if joker_count > 0 and hand_counter_len > 1:
            hand_counter_len -= 1

    else:
        hand_counter_len = len(hand_counter)
        joker_count = 0

    if hand_counter_len == 5:
        # high card
        return [0] + hand
    elif hand_counter_len == 4:

        # one pair
        return [1] + hand
    elif hand_counter_len == 3:
        if max(hand_counter.values()) + joker_count == 2:
            # 2 pair
            return [2] + hand
        elif max(hand_counter.values()) + joker_count in (3, 4):
            # 3 of a kind
            return [3] + hand

        else:
            raise ValueError()
    elif hand_counter_len == 2:
        if max(hand_counter.values()) + joker_count == 3:
            # full house
            return [4] + hand
        elif max(hand_counter.values()) + joker_count in (4, 6):
            # four of a kind
            return [5] + hand
        else:
            raise ValueError()
    elif hand_counter_len == 1:
        # five of a kind
        return [6] + hand
    else:
        raise ValueError()


def parse_line(line: str, joker=False):

    hand, bid = line.split(" ")
    bid = int(bid)
    hand_list = []

    for val in hand:
        if val.isnumeric():
            hand_list.append(int(val))
        elif val == "T":
            hand_list.append(10)
        elif val == "J":
            if joker:
                hand_list.append(1)
            else:
                hand_list.append(11)
        elif val == "Q":
            hand_list.append(12)
        elif val == "K":
            hand_list.append(13)
        elif val == "A":
            hand_list.append(14)
        else:
            raise ValueError("bad card value")

    return parse_hand(hand_list, joker=True)


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

    return sum(
        [
            (i + 1) * int(line.split(" ")[1])
            for i, line in enumerate(sorted(lines, key=parse_line))
        ]
    )


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return sum(
        [
            (i + 1) * int(line.split(" ")[1])
            for i, line in enumerate(
                sorted(lines, key=lambda x: parse_line(x, joker=True))
            )
        ]
    )


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_07.txt"))
    print(part_two("aoc/inputs/day_07.txt"))
