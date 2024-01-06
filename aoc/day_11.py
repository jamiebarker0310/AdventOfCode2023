import numpy as np
from itertools import combinations
from scipy import sparse


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

    data = np.vstack(
        [np.array([1 if char == "#" else 0 for char in line.strip()]) for line in lines]
    )

    data = np.insert(data, np.argwhere(data.sum(axis=0) == 0).T[0] + 1, 0, axis=1)
    data = np.insert(data, np.argwhere(data.sum(axis=1) == 0).T[0] + 1, 0, axis=0)

    stars = np.argwhere(data > 0)
    return sum([np.linalg.norm(p1 - p2, ord=1) for p1, p2 in combinations(stars, 2)])


def part_two(file_path: str, width=10 ** 6):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    X = np.vstack(
        [np.array([1 if char == "#" else 0 for char in line.strip()]) for line in lines]
    )
    n, m = X.shape

    insert1 = np.argwhere(X.sum(axis=0) == 0).T[0].tolist()
    insert2 = np.argwhere(X.sum(axis=1) == 0).T[0].tolist()

    X = sparse.csr_matrix(X)

    sparse_stacks = []
    for i, j in zip([0] + insert1, insert1 + [m]):
        sparse_stacks.append(X[:, i:j])
        sparse_stacks.append(sparse.csr_matrix((n, width - 1)))

    X = sparse.hstack(sparse_stacks[:-1], format="csr")

    n, m = X.shape
    sparse_stacks = []
    for i, j in zip([0] + insert2, insert2 + [n]):
        sparse_stacks.append(X[i:j, :])
        sparse_stacks.append(sparse.csr_matrix((width - 1, m)))

    X = sparse.vstack(sparse_stacks[:-1])

    return sum(
        [
            abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])
            for p1, p2 in combinations(zip(*X.nonzero()), 2)
        ]
    )


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_11.txt"))
    print(part_two("aoc/inputs/day_11.txt"))
