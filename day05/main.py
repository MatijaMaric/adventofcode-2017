
def solve(instructions):
    n = 0
    pos = 0
    while True:
        n += 1
        instruction = instructions[pos]
        instructions[pos] += 1
        pos += instruction
        if pos >= len(instructions):
            return n

def solve2(instructions):
    n = 0
    pos = 0
    while True:
        n += 1
        instruction = instructions[pos]
        if instructions[pos] >= 3:
            instructions[pos] -= 1
        else:
            instructions[pos] += 1
        pos += instruction
        if pos >= len(instructions):
            return n

if __name__ == '__main__':
    with open('day05/input.txt') as f:
        instructions = [int(x) for x in f.read().strip().split('\n')]

    steps = solve(instructions)
    print(steps)

    steps = solve2(instructions)
    print(steps)