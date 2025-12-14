"""
Advent of Code 2025: Day 12 puzzle
parse_input: parses input.txt into presents and regions
solve: computes number of "sparse" regions according to present sizes
puzzle1: prints the result for part 1
"""

def parse_input(filename):
    """Parse presents and regions from input file."""
    with open(filename) as f:
        data = f.read()

    parts = data.split('\n\n')
    presents_data = parts[:-1]
    regions_data = parts[-1]

    # --- compute sizes of each present ---
    present_sizes = {}
    for present in presents_data:
        lines = present.splitlines()
        # Present idx is first line minus colon
        name = int(lines[0][:-1])
        grid = [list(row) for row in lines[1:]]
        size = sum(1 for row in grid for c in row if c == '#')
        present_sizes[name] = size

    # --- parse regions ---
    regions = []
    for region in regions_data.splitlines():
        sz, ns = region.split(': ')
        R, C = map(int, sz.split('x'))
        ns = list(map(int, ns.split()))
        regions.append((R, C, ns))

    return present_sizes, regions


def solve(present_sizes, regions):
    """
    Counts regions where the total present size is sparse
    (i.e., total_present_size * 1.3 < grid size).
    """
    count = 0
    for R, C, ns in regions:
        total_present_size = sum(n * present_sizes[i] for i, n in enumerate(ns))
        total_grid_size = R * C

        if total_present_size * 1.3 < total_grid_size:
            count += 1
    return count


def puzzle1():
    present_sizes, regions = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 12/input.txt')
    print(solve(present_sizes, regions))

if __name__ == "__main__":
    puzzle1()
