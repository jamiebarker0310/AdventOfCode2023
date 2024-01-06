import networkx as nx
from tqdm import tqdm

def calculate_edge_dict(lines):

    edge_dict = {}

    n = len(lines)
    m = len(lines[0].strip())

    for i in range(n):
        for j in range(m):
            if lines[i][j] == "|":
                edge_dict[(i,j)] = [(i-1,j), (i+1,j)]
            elif lines[i][j] == "-":
                edge_dict[(i,j)] = [(i,j-1), (i,j+1)]
            elif lines[i][j] == "L":
                edge_dict[(i,j)] = [(i-1,j), (i,j+1)]
            elif lines[i][j] == "J":
                edge_dict[(i,j)] = [(i-1,j), (i,j-1)]
            elif lines[i][j] == "7":
                edge_dict[(i,j)] = [(i+1,j), (i,j-1)]
            elif lines[i][j] == "F":
                edge_dict[(i,j)] = [(i+1,j), (i,j+1)]
            elif lines[i][j] == ".":
                edge_dict[(i,j)] = []
            elif lines[i][j] == "S":
                start_point = (i,j)
                edge_dict[start_point] = []
            else:
                raise ValueError(lines[i][j])
    # for key, value in edge_dict.items():
    #     edge_dict[key] = [(i,j) for (i,j) in value if i>=0 and j>=0 and i<n and j<m]

    
    for key, value in edge_dict.items():
        for val in value:
            if val == start_point:
                edge_dict[start_point].append(key)
    
    return edge_dict, start_point

def calculate_path(lines):

    edge_dict, start_point = calculate_edge_dict(lines)

    path = [start_point]
    prev_point = start_point
    start_point, end_point = edge_dict[start_point]
    path.append(start_point)

    while start_point != end_point:
        start_point, prev_point = [n for n in edge_dict[start_point] if n != prev_point][0], start_point
        path.append(start_point)
    
    return path


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
    
    path = calculate_path(lines)
    
    return (len(path)//2)

def part_two(file_path: str):
    """[summary]

    Args:
        file_path (str): [description]

    Returns:
        [type]: [description]
    """

    with open(file_path) as f:
        lines = f.readlines()

    
    path = calculate_path(lines)

    n = len(lines)
    m = len(lines[0].strip())

    edge_dict = {}
    for i in range(-1, n+1):
        for j in range(-1, m+1):
            if (i,j) not in path:    
                edge_dict[(i,j)] = []
                for adjacent_node in [(i-1,j), (i+1,j), (i,j-1), (i,j+1)]:
                    if adjacent_node not in path:
                        edge_dict[(i,j)].append(adjacent_node)
            else:
                edge_dict[(i,j)] = []
    
    G = nx.from_dict_of_lists(edge_dict)

    nx.draw(G, pos={node: node for node in G.nodes})

    interior_nodes = []
    for node in tqdm(G.nodes):
        i,j = node
        if i>=0 and i<n and j>=0 and j<m:
            if node not in path:
                if nx.has_path(G, node, (-1,-1)):
                    interior_nodes.append(node)
        
    return len(interior_nodes)


if __name__ == "__main__":
    print(part_one("aoc/inputs/day_10.txt"))
    print(part_two("aoc/inputs/day_10.txt"))
