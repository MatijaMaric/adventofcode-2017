import re

def evaluate(cond, registers):
    conds = cond.split(' ')
    reg = conds[0]
    reg_val = registers[reg] if reg in registers else 0
    operator = conds[1]
    val = int(conds[2])
    if operator == '>':
        return reg_val > val
    if operator == '<':
        return reg_val < val
    if operator == '>=':
        return reg_val >= val
    if operator == '<=':
        return reg_val <= val
    if operator == '==':
        return reg_val == val
    if operator == '!=':
        return reg_val != val
    return None

def solve(instructions):
    registers = {}
    regex = re.compile(r'(\w+) (inc|dec) (-?\d+) if (.*)')
    max_val = float('-inf')
    for instruction in instructions:
        m = regex.match(instruction)
        reg = m.group(1)
        op = m.group(2)
        val = int(m.group(3))
        cond = m.group(4)
        if evaluate(cond, registers):
            if reg not in registers:
                registers[reg] = 0
            if op == 'inc':
                registers[reg] += val
            if op == 'dec':
                registers[reg] -= val
            if registers[reg] > max_val:
                max_val = registers[reg]
    
    return registers[max(registers, key=registers.get)], max_val

if __name__ == '__main__':
    with open('day08/input.txt') as f:
        instructions = f.readlines()

    ans, max_val = solve(instructions)
    print(ans)
    print(max_val)