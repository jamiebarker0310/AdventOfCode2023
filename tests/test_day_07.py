import pytest

from aoc.day_07 import parse_line, part_one, part_two


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_07.txt"

    assert part_one(test_file_path) == 6440


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_07.txt"

    assert part_two(test_file_path) == 5905


@pytest.mark.parametrize(
    "line,expected",
    (
        ("32T3K 765", [1, 3, 2, 10, 3, 13]),
        ("KK677 28", [2, 13, 13, 6, 7, 7]),
        ("T55J5 684", [5, 10, 5, 5, 1, 5]),
        ("KTJJT 789", [5, 13, 10, 1, 1, 10]),
        ("QQQJA 789", [5, 12, 12, 12, 1, 14]),
    ),
)
def test_parse_line(line, expected):

    assert parse_line(line, joker=True) == expected
