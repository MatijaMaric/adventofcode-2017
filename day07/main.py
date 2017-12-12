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

    regex = re.compile(r'^(\w+) \((\d+)\)(?: -> )?(.*)$')
    for line in towers:
        m = regex.match(line)
        parent = m.group(1)
        weight = int(m.group(2))
        child = m.group(3).split(', ') if m.group(3) else []
        
        weights[parent] = weight
        children[parent] = child

    return balance(root, weights, children)

def balance(node, weights, children):
    pairs = [(total_weight(child, weights, children), child) for child in children[node]]
    pairs = sorted(pairs, key=lambda x:-x[0])
    if pairs[0][0] == pairs[1][0]:
        return 0
    b = balance(pairs[0][1], weights, children)
    if b == 0:
        return weights[pairs[0][1]] - (pairs[0][0] - pairs[1][0])
    else:
        return b

def total_weight(node, weights, children):
    if len(children[node]) == 0:
        return weights[node]
    else:
        return weights[node] + sum([total_weight(child, weights, children) for child in children[node]])

if __name__ == '__main__':
    with open('day07/input.txt') as f:
        towers = f.readlines()
    
    root = solve(towers)
    print(root)

    weight = solve2(towers, root)
    print(weight)