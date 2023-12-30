import pytest

from aoc.day_01 import part_one, part_two, calc_exterior_digit_written


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_01.txt"

    assert part_one(test_file_path) == 142


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_01_b.txt"

    assert part_two(test_file_path) == 281


@pytest.mark.parametrize(
    "test_input,expected",
    [
        ("two1nine", 29),
        ("eightwothree", 83),
        ("abcone2threexyz", 13),
        ("xtwone3four", 24),
        ("4nineeightseven2", 42),
        ("zoneight234", 14),
        ("7pqrstsixteen", 76),
    ],
)
def test_calc_exterior_digit_written(test_input, expected):

    assert calc_exterior_digit_written(test_input) == expected
