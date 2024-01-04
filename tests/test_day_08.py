from aoc.day_08 import part_one, part_two

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_08.txt"

    assert part_one(test_file_path) == 2

def test_part_one_b():

    test_file_path = "tests/test_inputs/test_day_08_b.txt"

    assert part_one(test_file_path) == 6

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_08_c.txt"

    assert part_two(test_file_path) == 6