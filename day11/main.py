
def solve(directions):
    compass = {}
    compass['n']  = [ 0, -1]
    compass['ne'] = [ 1, -1]
    compass['se'] = [ 1,  0]
    compass['s']  = [ 0,  1]
    compass['sw'] = [-1,  1]
    compass['nw'] = [-1,  0]

    x, y = 0, 0
    max_dist = 0

    for d in directions:
        x += compass[d][0]
        y += compass[d][1]

        max_dist = max([max_dist, x, y])

    return max([abs(x), abs(y)]), max_dist
    
if __name__ == '__main__':
    with open('day11/input.txt') as f:
        directions = f.read().strip().split(',')
    
    steps, max_dist = solve(directions)
    print(steps)
    print(max_dist)