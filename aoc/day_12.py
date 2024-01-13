from itertools import combinations
def get_n_combinations(line: str):

    ".??..??...?##. 1,1,3" "4"
    line = line.strip()

    code, arrangements = line.split(" ")
    arrangements = list(map(int, arrangements.split(",")))

    code = list(code)

    qmarks = [i for i, x in enumerate(code) if x == "?"]

    count = 0
    for i in range(len(qmarks) + 1):
        for subset in combinations(qmarks, i):
            for q in qmarks:
                if q in subset:
                    code[q] = '#'
                else:
                    code[q] = '.'
            
            if check_arrangement(code, arrangements):
                count += 1
    
    return count
            
def check_arrangement(code, arrangements):

    total = 0
    calc_arrs = []
    for c in code:
        if c == ".":
            if total !=0:
                calc_arrs.append(total)
            total = 0
        elif c == "#":
            total += 1
        else:
            raise ValueError(c)
    if total !=0:
        calc_arrs.append(total)
    return calc_arrs == arrangements

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

    return sum([get_n_combinations(line) for line in lines])


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    return None


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_12.txt"))
    print(part_two("aoc/inputs/day_12.txt"))
