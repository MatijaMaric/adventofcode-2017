import re

def solve(towers):
    left = set()
    right = set()
    regex = re.compile(r'^(\w+) \((\d+)\)(?: -> )?(.*)$')
    for line in towers:
        m = regex.match(line)
        parent = m.group(1)
        weight = int(m.group(2))
        child = m.group(3).split(', ') if m.group(3) else []

        left.add(parent)
        right.update(child)
    
    diff = left.difference(right)
    return diff.pop()

def solve2(towers, root):
    weights = {}
    children = {}

    regex = re.compile('^(\w+) \((\d+)\)(?: -> )?(.*)$')
    for line in towers:
        m = regex.match(line)
        parent = m.group(1)
        weight = int(m.group(2))
        child = m.group(3).split(', ') if m.group(3) else []
        
        weights[parent] = weight
        children[parent] = child

if __name__ == '__main__':
    with open('day07/input.txt') as f:
        towers = f.readlines()
    
    root = solve(towers)
    print(root)

    weight = solve2(towers, root)
    print(weight)