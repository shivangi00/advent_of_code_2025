"""
Advent of Code 2025: Day 5 puzzle
parse_input: parses input data from input.txt file
puzzle1: brute force solution
puzzle2: generic and optimised solution
"""
#!/usr/bin/env python3
import sys
import bisect

def parse_input(lines):
    ranges = []
    ids = []
    it = iter(lines)
    # read ranges until blank line
    for line in it:
        line = line.strip()
        if line == "":
            break
        a,b = line.split("-")
        ranges.append((int(a), int(b)))
    # remaining lines are ids (ignore empty lines)
    for line in it:
        line = line.strip()
        if line:
            ids.append(int(line))
    return ranges, ids

def merge_ranges(ranges):
    if not ranges:
        return []
    # sort by start
    ranges = sorted(ranges, key=lambda x: x[0])
    merged = []
    cur_s, cur_e = ranges[0]
    for s,e in ranges[1:]:
        if s <= cur_e + 1:       # overlapping or adjacent
            cur_e = max(cur_e, e)
        else:
            merged.append((cur_s, cur_e))
            cur_s, cur_e = s, e
    merged.append((cur_s, cur_e))
    return merged

def is_fresh(merged, x):
    # merged is list of (s,e) disjoint, sorted by s
    # binary search to find right interval
    i = bisect.bisect_right(merged, (x, 10**18)) - 1
    if i >= 0:
        s,e = merged[i]
        return s <= x <= e
    return False

def main():
    if len(sys.argv) > 1:
        inp = open(sys.argv[1]).read().splitlines()
    else:
        inp = sys.stdin.read().splitlines()

    ranges, ids = parse_input(inp)
    merged = merge_ranges(ranges)

    count = sum(1 for x in ids if is_fresh(merged, x))
    print(count)

if __name__ == "__main__":
    main()
