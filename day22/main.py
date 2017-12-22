from collections import defaultdict

def solve(grid, iters, part2):
    ezgrid = defaultdict(lambda : '.')
    for i, line in enumerate(grid):
        for j, x in enumerate(line):
            ezgrid[(i, j)] = x
    
    directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
    posX, posY = len(grid) / 2, len(grid[0]) / 2
    infected = 0
    direction = 0

    for _ in range(iters):
        if ezgrid[posX, posY] == '#':
            direction = (direction + 1) % 4
            if part2:
                ezgrid[posX, posY] = 'f'
            else:
                ezgrid[posX, posY] = '.'
        elif ezgrid[posX, posY] == '.':
            direction = (direction - 1) % 4
            if part2:
                ezgrid[posX, posY] = 'w'
            else:
                infected += 1
                ezgrid[posX, posY] = '#'
        elif ezgrid[posX, posY] == 'w':
            ezgrid[posX, posY] = '#'
            infected += 1
        elif ezgrid[posX, posY] == 'f':
            ezgrid[posX, posY] = '.'
            direction = (direction + 2) % 4
        dirX, dirY = directions[direction]
        posX += dirX
        posY += dirY
    
    return infected

if __name__ == '__main__':
    with open('day22/input.txt') as f:
        grid = [list(x.strip()) for x in f.readlines()]
    
    infected = solve(grid, 10000, False)
    print(infected)

    infected = solve(grid, 10000000, True)
    print(infected)