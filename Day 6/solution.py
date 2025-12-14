"""
Advent of Code 2025: Day 6 puzzle
parse_input: parses input data from input.txt file
solve: computes part 1 and part 2
"""

def parse_input(filename):
    """Read the grid input from file."""
    with open(filename) as f:
        line = f.read()

    grid = [list(row) for row in line.splitlines()]
    return grid


def solve(grid):
    """
    Shared logic for both puzzles.
    Returns (p1, p2).
    """
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    puzzle1 = 0
    puzzle2 = 0

    start_col = 0

    while start_col < cols:
        # skip blank columns
        if all(grid[r][start_col] == ' ' for r in range(rows)):
            start_col += 1
            continue

        # find the end of the current block
        start = start_col
        while start_col < cols and not all(grid[r][start_col] == ' ' for r in range(rows)):
            start_col += 1
        end = start_col

        # extract operator
        op = grid[rows - 1][start]

        # solving puzzle1 
        val1 = 0 if op == '+' else 1
        for r in range(rows - 1):
            num = 0
            for ch in grid[r][start:end]:
                if ch != ' ':
                    num = num * 10 + int(ch)
            if op == '+':
                val1 += num
            else:
                val1 *= num
        puzzle1 += val1

        # solving puzzle2
        val2 = 0 if op == '+' else 1
        block = []
        for rown in grid[:-1]:
            block.append(rown[start:end])
        for col in reversed(list(zip(*block))):
            num = 0
            for ch in col:
                if ch != ' ':
                    num = num * 10 + int(ch)
            if op == '+':
                val2 += num
            else:
                val2 *= num
        puzzle2 += val2
    
    return puzzle1, puzzle2

def puzzle1():
    grid = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 6/input.txt')
    p1, _ = solve(grid)
    print(p1)


def puzzle2():
    grid = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 6/input.txt')
    _, p2 = solve(grid)
    print(p2)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
