"""
Advent of Code 2025: Day 7 puzzle
parse_input: parses input data from input.txt file
puzzle1: computes part 1 score
puzzle2: computes part 2 score
"""

from functools import cache
def parse_input(filename):
    """Read grid and locate start position."""
    with open(filename) as f:
        grid = [list(row) for row in f.read().splitlines()]

    for r, row in enumerate(grid):
        for c, val in enumerate(row):
            if val == 'S':
                return grid, r, c

    # Default to top-left if 'S' not found
    return grid, 0, 0


def total_splits(grid, sr, sc):
    """ BFS traversal counting splits (^)"""
    from collections import deque

    rows = len(grid)
    queue = deque([(sr, sc)])
    seen = set()
    total = 0

    while queue:
        r, c = queue.popleft()
        if (r, c) in seen:
            continue
        seen.add((r, c))

        if r + 1 == rows:
            continue

        if grid[r + 1][c] == '^':
            queue.append((r + 1, c - 1))
            queue.append((r + 1, c + 1))
            total += 1
        else:
            queue.append((r + 1, c))

    return total


def total_paths(grid, sr, sc):
    """ Memoized recursive DP for total paths."""
    rows = len(grid)

    @cache
    def dfs(r, c):
        if r + 1 == rows:
            return 1
        if grid[r + 1][c] == '^':
            return dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        return dfs(r + 1, c)

    return dfs(sr, sc)


def puzzle1():
    grid, sr, sc = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 7/input.txt')
    print(total_splits(grid, sr, sc))


def puzzle2():
    grid, sr, sc = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 7/input.txt')
    print(total_paths(grid, sr, sc))


if __name__ == "__main__":
    puzzle1()
    puzzle2()
