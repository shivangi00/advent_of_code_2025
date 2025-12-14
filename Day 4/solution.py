"""
Advent of Code 2025: Day 4 puzzle
parse_input: parses input data from input.txt file
puzzle1: brute force solution
puzzle2: generic and optimised solution
"""

def parse_input(filename):
    ranges = []
    ids = []
    with open(filename) as f:
        lines = [line.strip() for line in f]

    reading_ranges = True
    for line in lines:
        if line == "":
            reading_ranges = False
            continue
        if reading_ranges:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            ids.append(int(line))

    return ranges, ids


def brute_force_fresh_count(ranges, ids):
    """Puzzle 1: Count how many available IDs are fresh."""
    fresh = 0
    for x in ids:
        for a, b in ranges:
            if a <= x <= b:
                fresh += 1
                break
    return fresh


def merge_ranges(ranges):
    """Helper for aggregated ranges."""
    if not ranges:
        return []

    ranges = sorted(ranges)
    merged = []
    s, e = ranges[0]

    for a, b in ranges[1:]:
        if a <= e + 1:      # overlapping or touching
            e = max(e, b)
        else:
            merged.append((s, e))
            s, e = a, b
    merged.append((s, e))

    return merged


def count_total_fresh_ids(ranges):
    """Puzzle 2: Count the total number of distinct fresh IDs."""
    merged = merge_ranges(ranges)
    total = 0
    for s, e in merged:
        total += (e - s + 1)   # inclusive range
    return total


def puzzle1():
    ranges, ids = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 5/input.txt')
    result = brute_force_fresh_count(ranges, ids)
    print(result)


def puzzle2():
    ranges, ids = parse_input('/Users/shivangimalik/Documents/advent_of_code_2025/Day 5/input.txt')
    result = count_total_fresh_ids(ranges)
    print(result)


if __name__ == "__main__":
    puzzle1()
    puzzle2()
