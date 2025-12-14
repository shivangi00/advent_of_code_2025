from functools import lru_cache

def parse_input(filename):
    server_map = {}
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            parts = line.split(": ")
            server_map[parts[0]] = parts[1].split(" ")
    return server_map

def find_path(server_map, start, target):
    total = 0
    stack = [(start, {start})]
    while stack:
        current, visited = stack.pop()
        if current == target:
            total += 1
            continue
        for neighbour in server_map.get(current, []):
            if neighbour not in visited:
                stack.append((neighbour, visited | {neighbour}))
    return total

def count_paths_dp(graph, start, target):
    # encode: 1 = dac, 2 = fft
    def update_mask(node, mask):
        if node == "dac": mask |= 1
        if node == "fft": mask |= 2
        return mask

    @lru_cache(None)
    def dfs(node, mask):
        mask = update_mask(node, mask)

        if node == target:
            return 1 if mask == 3 else 0

        total = 0
        for nxt in graph.get(node, []):
            total += dfs(nxt, mask)

        return total

    return dfs(start, 0)

def puzzle1():
    # Change this to your input file path
    server_map = parse_input("/Users/shivangimalik/Documents/advent_of_code_2025/Day 11/input.txt")
    start = "you"
    target = "out"
    result = find_path(server_map, start, target)
    print(result)


def puzzle2():
    server_map = parse_input("/Users/shivangimalik/Documents/advent_of_code_2025/Day 11/input.txt")
    start = "svr"
    target = "out"
    result = result = count_paths_dp(server_map, start, target)
    print(result)

if __name__ == "__main__":
    puzzle1()
    puzzle2()