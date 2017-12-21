import copy

def rotate(pattern):
    size = len(pattern)
    ans = []
    for _ in range(4):
        pattern = symmetric(pattern)
        ans.append(tuple([''.join(x) for x in pattern]))
        pattern = flip(pattern)
        ans.append(tuple([''.join(x) for x in pattern]))
        
    return ans 

def flip(pattern):
    new_pattern = copy.deepcopy(pattern)
    size = len(pattern)
    for i in range(size):
        for j in range(size):
            new_pattern[i][j] = pattern[i][size-j-1]
    return new_pattern

def symmetric(pattern):
    new_pattern = copy.deepcopy(pattern)
    size = len(pattern)
    for i in range(size):
        for j in range(size):
            new_pattern[i][j] = pattern[j][i]
    return new_pattern

def parse(lines):
    rules = {}

    for line in lines:
        _in, _out = line.split(' => ')
        _in = [list(x) for x in _in.split('/')]
        output = tuple(_out.strip().split('/'))
        inputs = rotate(_in)
        for input in inputs:
            rules[input] = output

    return rules

def count(pattern):
    return sum([sum([(1 if x == '#' else 0) for x in line]) for line in pattern])

def expand(pattern, rules):
    size = len(pattern)
    if size % 2 == 0:
        segment_size = 2
    else:
        segment_size = 3
    grid = [list(x) for x in pattern]
    
    segments = []
    segments_size = size/segment_size
    for i in range(segments_size):
        segment_row = []
        for j in range(segments_size):
            segment = tuple([''.join([grid[i*segment_size+x][j*segment_size+y] for y in range(segment_size)]) for x in range(segment_size)])
            segment = rules[segment]
            segment_row.append(segment)
        segments.append(segment_row)
    
    size = size/segment_size*(segment_size+1)
    new_grid = [[None]*size for _ in range(size)]

    for i in range(size):
        for j in range(size):
            new_grid[i][j] = segments[i/(segment_size+1)][j/(segment_size+1)][i%(segment_size+1)][j%(segment_size+1)]
    
    new_pattern = tuple([''.join(row) for row in new_grid])
    return new_pattern

def times(fx, args, n):
    ans = args[0]
    for _ in range(n):
        ans = fx(ans, args[1])
    return ans

if __name__ == '__main__':
    with open('day21/input.txt') as f:
        rules = parse(f.readlines())

    pattern = ('.#.', '..#', '###')
    pixels = count(times(expand, (pattern, rules), 5))
    print(pixels)
    pixels = count(times(expand, (pattern, rules), 18))
    print(pixels)
    