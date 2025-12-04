"""
Advent of Code 2025: Day 1 puzzle
parse_input: parses input data from input.txt file
"""

def parse_input(filename):
    rotations = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            direction = line[0]
            distance = int(line[1:])
            rotations.append([direction, distance])
    return rotations

def find_zeros(rotations, dial, full_dial=100, zeros_crossed=False):
    total_zeros = 0
    for rotation in rotations:
        # if distance is more than 100, adjust its value
        if rotation[1] > full_dial:
            # if puzzle2: add up number of times zero is crossed
            if zeros_crossed:
                total_zeros += rotation[1] // full_dial
            rotation[1] = rotation[1] % full_dial

        if rotation[0] == "L":
            turn = dial - rotation[1]
            # if the dial turns to negative value, 
            # correct it by adding 100
            # eg 50-60 = -10 => 100-10 = 90
            if turn < 0:
                if zeros_crossed and dial > 0:
                    total_zeros += 1
                turn = turn + full_dial
        else:
            turn = dial + rotation[1]
            # if the dial turns to value more than 100 or to 100
            # correct it by dividing by 100 and using the remainder
            # eg 100% 100 = 0
            if turn >= full_dial:
                if zeros_crossed and turn != full_dial:
                    total_zeros += 1
                turn = turn % full_dial
        
        dial = turn
        
        # add number of zeros whenever dial turns to zero
        if dial == 0:
            total_zeros += 1

    return total_zeros

def puzzle1():
    rotations = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 1/input.txt")
    dial = 50
    ans = find_zeros(rotations, dial)
    print(ans)

def puzzle2():
    rotations = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 1/input.txt")
    dial = 50
    ans = find_zeros(rotations, dial, 100, True)
    print(ans)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
