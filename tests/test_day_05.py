from aoc.day_05 import part_one, part_two, condition, split_range
import pytest

# @pytest.mark.parametrize()
def test_condition():

    assert condition(53, False, 49, 53, 8) == (49, True)


def test_part_one():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    assert part_one(test_file_path) == 35

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_05.txt"

    assert part_two(test_file_path) == 46

def test_split_range():

    changed, unchanged =  split_range(57, 70, 49, 53, 8)

    assert changed == ((53, 57),)
    assert unchanged == ((61, 70),)

    changed, unchanged =  split_range(90, 99, 60, 56, 37)

    assert changed == ((94, 97),)
    assert unchanged == ((93, 99),)



