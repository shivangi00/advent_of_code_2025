"""
Advent of Code 2025: Day 8 puzzle
puzzle1: prints Part 1 result
puzzle2: prints Part 2 result
"""

from collections import defaultdict

def parse_input(filename):
    """Read 3D points from input file."""
    points = []
    with open(filename) as f:
        for line in f:
            x, y, z = map(int, line.strip().split(','))
            points.append((x, y, z))
    return points


def solve(points):
    # --- compute pairwise distances ---
    distances = []
    for i, (x1, y1, z1) in enumerate(points):
        for j, (x2, y2, z2) in enumerate(points):
            if i > j:
                d = (x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2
                distances.append((d, i, j))
    distances.sort()

    # --- Union-Find setup ---
    UF = {i: i for i in range(len(points))}

    def find(x):
        if UF[x] != x:
            UF[x] = find(UF[x])
        return UF[x]

    def union(x, y):
        UF[find(x)] = find(y)

    connections = 0
    puzzle1_result = None
    puzzle2_result = None

    for t, (_d, i, j) in enumerate(distances):
        if t == 1000:
            # Compute largest 3 component sizes
            SZ = defaultdict(int)
            for x in range(len(points)):
                SZ[find(x)] += 1
            S = sorted(SZ.values())
            puzzle2_result = S[-1] * S[-2] * S[-3]

        if find(i) != find(j):
            connections += 1
            if connections == len(points) - 1:
                # Use x-coordinates of last connected points as Part 1
                puzzle1_result = points[i][0] * points[j][0]
            union(i, j)

    return puzzle1_result, puzzle2_result


def puzzle1():
    points = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 8/input.txt')
    print(solve(points)[0])


def puzzle2():
    points = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 8/input.txt')
    print(solve(points)[1])


if __name__ == "__main__":
    puzzle1()
    puzzle2()
