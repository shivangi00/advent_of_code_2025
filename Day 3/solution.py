"""
Advent of Code 2025: Day 3 puzzle
parse_input: parses input data from input.txt file
puzzle1: brute force solution
puzzle2: generic and optimised solution
"""

def parse_input(filename):
    banks = []
    with open(filename) as f:
        for line in f:
            line = line.strip()
            banks.append(int(line))
    return banks

def sum_2_largest(banks):
    sum = 0
    for bank in banks:
        max = 0
        # convert input number data to a list of numbers
        bank_list = list(map(int, str(bank)))
        # find largest two numbers without changing order of list
        for i in range(len(bank_list)):
            for j in range(i + 1, len(bank_list)):
                # convert the numbers to a two digit number
                val = bank_list[i] * 10 + bank_list[j]
                # update value of max
                if val > max:
                    max = val
        sum += max
    return sum

def sum_n_largest(banks, n):
    sum = 0
    # using stack
    for bank in banks:
        stack = []
        # convert input number data to a list of numbers
        num_list = list(map(int, str(bank)))
        # number of maximum deletions from the input
        deletions = len(num_list) - n
        for num in num_list:
            # while we can perform deletions and stack is not empty 
            # and top value of stack is less than current number, 
            # perform pop from stack
            while deletions and stack and stack[-1] < num:
                stack.pop()
                deletions -= 1
            stack.append(num)
        # take only the first n digits
        result_num = stack[:n]
        # convert to int
        val = 0
        for res_num in result_num:
            val = val * 10 + res_num
        sum += val        
    return sum

def puzzle1():
    banks = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 3/input.txt")
    result = sum_2_largest(banks)
    print(result)

def puzzle2():
    banks = parse_input("/Users/shivangimalik/Documents/Advent of Code/Day 3/input.txt")
    n = 12
    result = sum_n_largest(banks, n)
    print(result)

if __name__ == "__main__":
    puzzle1()
    puzzle2()
