from collections import defaultdict

bridges = set()

def solve(links):
    graph = defaultdict(lambda : [])
    for link in links:
        graph[link[0]].append(link[1])
        graph[link[1]].append(link[0])
        
    strongest_bridge = 0
    for root in graph[0]:
        visited = [(0, root)]
        strongest_bridge = max(strongest_bridge, strongest(graph, visited))
    
    return strongest_bridge

def solve2(bridges):
    length = 0
    strength = 0
    while len(bridges) > 0:
        bridge = bridges.pop()
        if len(bridge) >= length:
            _strength = sum(a+b for a, b in bridge)
            if _strength > strength:
                length = len(bridge)
                strength = _strength
    
    return strength

def strongest(graph, visited):
    last = visited[-1]
    port = last[1]
    bridges.add(tuple(visited))
    strongest_bridge = sum(a+b for a, b in visited)
    for node in graph[port]:
        if (port, node) not in visited and (node, port) not in visited:
            _visited = visited[:]
            _visited.append((port, node))
            strongest_bridge = max(strongest_bridge, strongest(graph, _visited))
    return strongest_bridge  

if __name__ == '__main__':
    with open('day24/input.txt') as f:
        links = [tuple(int(x) for x in line.strip().split('/')) for line in f.readlines()]
    
    strongest = solve(links)
    print(strongest)

    longest = solve2(bridges)
    print(longest)   
