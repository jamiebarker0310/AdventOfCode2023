from aoc.day_10 import part_one, part_two

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_10.txt"

    assert part_one(test_file_path) == 8

def test_part_two_b():

    test_file_path = "tests/test_inputs/test_day_10_b.txt"

    assert part_two(test_file_path) == 4

def test_part_two_c():

    test_file_path = "tests/test_inputs/test_day_10_c.txt"

    assert part_two(test_file_path) == 10