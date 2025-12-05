"""
Advent of Code 2025: Day 4 puzzle
parse_input: parses input data from input.txt file
puzzle1: brute force solution
puzzle2: generic and optimised solution
"""

def parse_input(filename):
    grid = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            grid.append(list(line))
    return grid

def total_rolls(grid, puzzle):
    sum = 0
    max_rolls_removed = 0
    rows = len(grid)
    cols = len(grid[0])

    while True:
        rolls_removed = False
        for row in range(rows):
            for col in range(cols):
                adj_rolls = 0

                for dir_r in [-1, 0, 1]:
                    for dir_c in [-1, 0, 1]:
                        nr, nc = row + dir_r, col + dir_c

                        if 0 <= nr < rows and 0 <= nc < cols:
                            if grid[nr][nc] == "@":
                                adj_rolls += 1
                        
                if grid[row][col] == "@" and adj_rolls < 5:
                    sum += 1
                    rolls_removed = True
                    if puzzle == 2:
                        grid[row][col] = '.'
                        max_rolls_removed += 1
        if not rolls_removed:
            break
    
        if puzzle == 1:
            return sum
    return max_rolls_removed


def puzzle1():
    grid = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 4/input.txt")
    result = total_rolls(grid, 1)
    print(result)

def puzzle2():
    grid = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 4/input.txt")
    result = total_rolls(grid, 2)
    print(result)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
