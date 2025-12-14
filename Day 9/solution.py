from itertools import combinations

def parse_input(filename):
    coordinates = []
    with open(filename) as f:
        for line in f:
            x, y = map(int, line.strip().split(","))
            coordinates.append((x, y))
    return coordinates

def largest_rect_exclude_lines(coordinates):
    """
    https://github.com/ChristopherBiscardi/advent-of-code/blob/16f6745671af5ac38f8e128819fa3fc8f2f7534a/2025/rust/day-09/src/part2.rs
    - coordinates: list of (x, y) red tiles
    - Returns largest rectangle area where rectangle does NOT intersect any polygon edges
    """
    max_area = 0
    best_pair = None

    n = len(coordinates)
    # Build "lines" between consecutive red tiles (closed loop)
    lines = [(coordinates[i], coordinates[(i + 1) % n]) for i in range(n)]

    # Check all pairs of red tiles
    for a, b in combinations(coordinates, 2):
        x1, y1 = a
        x2, y2 = b
        area = (abs(x1 - x2) + 1) * (abs(y1 - y2) + 1)

        # Check rectangle vs all lines
        valid = True
        for (lx1, ly1), (lx2, ly2) in lines:
            # Rectangle edges
            rect_left = min(x1, x2)
            rect_right = max(x1, x2)
            rect_bottom = min(y1, y2)
            rect_top = max(y1, y2)

            # Line bounding box
            line_left = min(lx1, lx2)
            line_right = max(lx1, lx2)
            line_bottom = min(ly1, ly2)
            line_top = max(ly1, ly2)

            # Check if line is completely outside rectangle
            if rect_right <= line_left or rect_left >= line_right \
               or rect_top <= line_bottom or rect_bottom >= line_top:
                continue  # line does not intersect rectangle
            else:
                valid = False
                break

        if valid and area > max_area:
            max_area = area
            best_pair = (a, b)

    print("Largest rectangle area (Python version):", max_area)
    print("Using red tiles:", best_pair)
    return max_area

# ----------------------
# Puzzle wrappers
# ----------------------
def puzzle1():
    coordinates = parse_input("/Users/shivangimalik/Documents/advent_of_code_2025/Day 9/input.txt")
    # Simple largest rectangle ignoring polygon
    max_area = 0
    best_pair = None
    for a, b in combinations(coordinates, 2):
        x1, y1 = a
        x2, y2 = b
        area = abs(x1 - x2) * abs(y1 - y2)
        if area > max_area:
            max_area = area
            best_pair = (a, b)
    print("Puzzle 1 area:", max_area, best_pair)

def puzzle2():
    coordinates = parse_input("/Users/shivangimalik/Documents/advent_of_code_2025/Day 9/input.txt")
    result = largest_rect_exclude_lines(coordinates)
    print(result)


if __name__ == "__main__":
    puzzle1()
    puzzle2()