"""
Advent of Code 2025: Day 2 puzzle
parse_input: parses input data from input.txt file
puzzle1: brute force solution
puzzle2: generic and optimised solution
"""

def load_input(filename):
    with open(filename) as f:
        for line in f:
            line = line.strip()
            product_ids = line.split(",")
    return product_ids

def invalid_ids(product_ids):
    sum = 0
    for id in product_ids:
        # get start and end of the range of ids
        start_id_range, end_id_range = int(id.split("-")[0]), int(id.split("-")[-1])
        for num in range(start_id_range, end_id_range + 1):
            num = str(num)
            # check for even ids
            if len(num) % 2 == 0:
                # check whether the two halves of the id are same or not
                # add if true
                half = len(num) // 2
                if num[0:half] == num[half:]:
                    sum += int(num)
    return sum

def invalid_ids_generic(product_ids):
    total = 0
    for id in product_ids:
        # get start and end of the range of ids
        start_id_range, end_id_range = int(id.split("-")[0]), int(id.split("-")[-1])
        for num in range(start_id_range, end_id_range + 1):
            s = str(num)
            n = len(s)
            # Try each possible block size m that divides n
            # such that k = n // m is at least 2 and m cannot be n
            for m in range(1, n):
                if n % m != 0:
                    continue
                
                k = n // m
                if k < 2:
                    continue
                
                block = s[:m]
                
                if block * k == s:   # repeated pattern check
                    total += num
                    break  # stop checking once num is invalid
    return total

def puzzle1():
    product_ids = load_input("/Users/shivangimalik/Documents/Advent of Code/Day 2/input.txt")
    result = invalid_ids(product_ids)
    print(result)

def puzzle2():
    product_ids = load_input("/Users/shivangimalik/Documents/Advent of Code/Day 2/input.txt")
    result = invalid_ids_generic(product_ids)
    print(result)

if __name__ == "__main__":
    puzzle1()
    puzzle2()