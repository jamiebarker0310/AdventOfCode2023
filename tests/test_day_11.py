from aoc.day_11 import part_one, part_two


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_one(test_file_path) == 374


def test_part_two():

    test_file_path = "tests/test_inputs/test_day_11.txt"

    assert part_two(test_file_path, width=10) == 1030
    assert part_two(test_file_path, width=100) == 8410
