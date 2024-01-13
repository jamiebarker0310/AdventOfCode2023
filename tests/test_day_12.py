import pytest

from aoc.day_12 import part_one, part_two, get_n_combinations, check_arrangement

def test_get_n_combinations():

    assert get_n_combinations("???.### 1,1,3") == 1

@pytest.mark.parametrize("code, args",
                         (
                             (list(".###.##.#..."), [3,2,1]),
                             (list("#.#.###"), [1,1,3])
                         )
                         )
def test_check_arrangement(code, args):

    assert check_arrangement(code, args)

def test_part_one():

    test_file_path = "tests/test_inputs/test_day_12.txt"

    assert part_one(test_file_path) == 21

def test_part_two():

    test_file_path = "tests/test_inputs/test_day_12.txt"

    assert part_two(test_file_path)