from collections import deque

def parse(pipes):
    groups = {}

    for pipe in pipes:
        [left, right] = pipe.split(' <-> ')
        left = int(left)
        right = [int(x) for x in right.split(', ')]
        
        if left not in groups:
            groups[left] = set() 
        groups[left] |= set(right)
    
    return groups

def solve(groups):    
    return len(visit(0, groups))

def visit(node, groups):
    visited = set()
    q = deque()
    q.append(node)
    while len(q) > 0:
        current = q.pop()
        visited.add(current)
        for next in groups[current]:
            if next not in visited:
                q.append(next)
    
    return visited

def count_groups(groups):
    unvisited = set(groups.keys())
    ans = 0
    while len(unvisited) > 0:
        unvisited -= visit(unvisited.pop(), groups)
        ans += 1
    return ans

if __name__ == '__main__':
    with open('day12/input.txt') as f:
        pipes = f.readlines()
    
    groups = parse(pipes)

    programs = solve(groups)
    print(programs)

    group_count = count_groups(groups)
    print(group_count)

