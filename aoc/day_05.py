def condition(x, changed, dest, source, length):
    if changed:
        return x, True
    elif x - source < length and x >= source:
        return x - source + dest, True
    else:
        return x, False


def apply_mappings(maps, seeds):

    # and we have mapping functions
    if len(maps) > 0:
        # initialise new seeds
        new_seeds = []
        # for each of the seeds
        for seed in seeds:
            # initialise changed to False
            changed = False
            # for each mapping function
            for map_func in maps:
                # apply the mapping function
                dest, source, length = map_func
                seed, changed = condition(seed, changed, dest, source, length)
            # append the adjusted seed to new seeds
            new_seeds.append(seed)
        # set the seeds to the new seeds
        seeds = new_seeds

    return seeds


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

    seeds = lines[0]
    seeds = [
        int(x.strip()) for x in seeds[seeds.index(": ") + 1 :].split(" ") if len(x) > 0
    ]
    maps = []
    for i in range(1, len(lines)):
        # if it's an empty line
        if len(lines[i].strip()) == 0:
            seeds = apply_mappings(maps, seeds)
            # initialise
            maps = []

        elif len(lines[i].split(" ")) == 3:
            dest, source, length = map(int, lines[i].split(" "))
            maps.append((dest, source, length))

    seeds = apply_mappings(maps, seeds)

    return min(seeds)


def split_range(xmin, xmax, dest, source, length) -> tuple:

    # if xmin is less than the source
    if xmin < source:
        # and xmax is less than or equal to the source
        if xmax <= source:
            # none are changed
            changed = ()
            unchanged = ((xmin, xmax),)
        # if xmax is greater than source and leq
        elif xmax > source and xmax <= source + length:
            changed = ((dest, dest + xmax - source),)
            unchanged = ((xmin, source),)
        # if xmax is bigger than the source and length
        elif xmax > source + length:
            # the whole destination range has changed
            changed = ((dest, dest + length),)
            # outside the range has changed
            unchanged = ((xmin, source), (source + length, xmax))
        else:
            raise ValueError("RUHROH")
    # elif xmin is geq than source and less than source + length
    elif xmin >= source and xmin < source + length:
        # if xmax leq than source + length
        if xmax <= source + length:
            # then the changed ranged is the adjusted range
            changed = ((xmin + dest - source, xmax + dest - source),)
            # nothing is unchanged
            unchanged = ()
        # if xmax is greater than the source length
        elif xmax > source + length:
            # nothing is adjusted xmin to the max dest length is changed
            changed = ((xmin + dest - source, dest + length),)
            # the top of source length to xmax remains unchanged
            unchanged = ((source + length, xmax),)

        else:
            raise ValueError("RUHROH")

    # if xmin is geq source + length
    elif xmin >= source + length:
        # then obviously
        if xmax > source + length:
            # nothing is changed
            changed = ()
            # xmin and xmax are unchanged
            unchanged = ((xmin, xmax),)

        else:
            raise ValueError("RUHROH")

    else:
        raise ValueError("RUHROH")

    return changed, unchanged


def compute_lengths(seeds):

    return sum([b - a for a, b in seeds])


def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    seeds = lines[0]
    seeds = [
        int(x.strip()) for x in seeds[seeds.index(": ") + 1 :].split(" ") if len(x) > 0
    ]
    seeds = [(seeds[i], seeds[i] + seeds[i + 1]) for i in range(0, len(seeds), 2)]

    original_lengths = compute_lengths(seeds)

    changed_seeds = []
    unchanged_seeds = []

    # for each line
    for i in range(2, len(lines)):
        # if it's a mapping line
        if len(lines[i].split(" ")) == 3:
            # parse the mapping arguments
            dest, source, length = map(int, lines[i].split(" "))
            # for each seed range that hasn't yet been adjusted
            for xmin, xmax in seeds:
                # get the changed ranges and the unchanged ranges
                changed, unchanged = split_range(xmin, xmax, dest, source, length)
                # append the changed seeds to the changed seeds list
                for c in changed:
                    changed_seeds.append(c)
                # append the unchanged seeds to the unchanged seeds list
                for u in unchanged:
                    unchanged_seeds.append(u)
            seeds = unchanged_seeds
            unchanged_seeds = []
        # if it's an empty line
        if len(lines[i].strip()) == 0:
            # set the seeds to the changed seeds and unchanged seeds
            seeds = seeds + changed_seeds
            unchanged_seeds = []
            changed_seeds = []

    seeds = seeds + changed_seeds
    unchanged_seeds = []
    changed_seeds = []

    return min(seeds)[0]


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_05.txt"))
    print(part_two("aoc/inputs/day_05.txt"))
