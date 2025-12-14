import z3

def parse_line(line):
    """Parse a single line into diagram and buttons as bitmasks."""
    parts = line.split()
    diagram = parts[0][1:-1]
    buttons = []
    for part in parts[1:]:
        if part.startswith('(') and part.endswith(')'):
            content = part[1:-1].strip()
            if content == "":
                buttons.append(0)
            else:
                # Convert button to bitmask integer
                mask = sum(1 << int(x) for x in content.split(','))
                buttons.append(mask)
        else:
            break  # stop at {joltage}
    return diagram, buttons

def parse_line_part2(line):
    """Parse a line for part 2: extract buttons as lists and joltage targets."""
    parts = line.split()
    
    # Parse buttons
    buttons = []
    for part in parts[1:]:
        if part.startswith('(') and part.endswith(')'):
            content = part[1:-1].strip()
            if content == "":
                buttons.append([])
            else:
                buttons.append([int(x) for x in content.split(',')])
        else:
            break
    
    # Parse joltage requirements (last part in {})
    joltage_str = parts[-1]
    joltage = [int(x) for x in joltage_str[1:-1].split(',')]
    
    return buttons, joltage

def min_presses(diagram, buttons):
    """Compute minimal presses for a single machine using DFS and bitmask."""
    # Convert diagram to integer bitmask
    goal = 0
    for i, c in enumerate(diagram):
        if c == '#':
            goal |= 1 << i

    m = len(buttons)
    best = [m + 1]  # max presses can't exceed number of buttons

    def dfs(idx, state, presses):
        if presses >= best[0]:
            return
        if idx == m:
            if state == goal:
                best[0] = presses
            return
        # Option 1: skip button
        dfs(idx + 1, state, presses)
        # Option 2: press button
        dfs(idx + 1, state ^ buttons[idx], presses + 1)

    dfs(0, 0, 0)
    return best[0]


def min_presses_part2(buttons, joltage):
    """
    Solve part 2 using Z3 optimizer.
    Find minimum button presses to reach exact joltage levels.
    """
    # Create Z3 variables for button press counts
    V = []
    for i in range(len(buttons)):
        V.append(z3.Int(f'B{i}'))
    
    # Create optimizer
    o = z3.Optimize()
    
    # Minimize total button presses
    o.minimize(z3.Sum(V))
    
    # Add constraints: each joltage counter must reach its target
    for counter_idx in range(len(joltage)):
        # Sum all button presses that affect this counter
        terms = []
        for button_idx in range(len(buttons)):
            if counter_idx in buttons[button_idx]:
                terms.append(V[button_idx])
        
        # This counter must equal its target value
        if terms:
            o.add(z3.Sum(terms) == joltage[counter_idx])
        else:
            # If no button affects this counter, it must be 0
            o.add(joltage[counter_idx] == 0)
    
    # All button presses must be non-negative
    for v in V:
        o.add(v >= 0)
    
    # Solve
    if o.check() == z3.sat:
        M = o.model()
        total = 0
        for v in V:
            total += M[v].as_long()
        return total
    else:
        return 0  # No solution found

def total_minimum_presses(filename):
    """Compute total minimum presses for all machines in the file."""
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            diagram, buttons = parse_line(line)
            total += min_presses(diagram, buttons)
    return total

def total_minimum_presses_part2(filename):
    """Compute total minimum presses for part 2."""
    total = 0
    with open(filename) as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            buttons, joltage = parse_line_part2(line)
            total += min_presses_part2(buttons, joltage)
    return total

def puzzle1():
    # Change this to your input file path
    filename = "/Users/shivangimalik/Documents/advent_of_code_2025/Day 10/input.txt"
    result = total_minimum_presses(filename)
    print(result)


def puzzle2():
    filename = "/Users/shivangimalik/Documents/advent_of_code_2025/Day 10/input.txt"
    result = total_minimum_presses_part2(filename)
    print(result)

if __name__ == "__main__":
    puzzle1()
    puzzle2()