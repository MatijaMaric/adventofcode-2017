import itertools

def run(instructions, debug):
    registers = {}
    if debug:
        registers['a'] = 1
    pos = 0
    count = 0

    def value(x):
        try:
            return int(x)
        except ValueError:
            if x in registers:
                return registers[x]
            else:
                return 0

    while True:
        instruction = instructions[pos].strip().split(' ')
        if instruction[0] == 'set':
            registers[instruction[1]] = value(instruction[2])
        if instruction[0] == 'sub':
            if instruction[1] in registers:
                registers[instruction[1]] -= value(instruction[2])
            else:
                registers[instruction[1]] = -value(instruction[2])
        if instruction[0] == 'mul':
            if instruction[1] in registers:
                registers[instruction[1]] *= value(instruction[2])
            else:
                registers[instruction[1]] = 0
            count += 1
        if instruction[0] == 'jnz':
            if value(instruction[1]) != 0:
                pos += value(instruction[2])
            else:
                pos += 1
        else:
            pos += 1
        if pos >= len(instructions):
            break
    if debug:
        return registers['h']
    else:
        return count

def count_composites(start, end, step):
    primes = generate_primes(end)
    count = 0
    for i in range(start, end, step):
        if i not in primes:
            count += 1
    return count

def generate_primes(max_num):
    numbers = set(range(max_num, 1, -1))
    primes = []
    while numbers:
        p = numbers.pop()
        primes.append(p)
        numbers.difference_update(range(p*2, max_num+1, p))
    return primes

if __name__ == '__main__':
    with open('day23/input.txt') as f:
        instructions = f.readlines()
    
    execute = run(instructions, False)
    print(execute)

    b = 81 * 100 + 100000
    c = b + 17000

    primes = count_composites(b, c+1, 17)
    print(primes)