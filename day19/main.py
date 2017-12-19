
def solve(grid):
    width = len(grid[0])
    height = len(grid)

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    x, y = 0, 0
    dirX, dirY = directions[0]

    for i in range(width):
        if grid[0][i] == '|':
            x = 0
            y = i
            break

    sequence = ""
    steps = 0

    while True:
        steps += 1
        x += dirX
        y += dirY
        if grid[x][y] == '+':
            for turnX, turnY in directions:
                if (dirY == 0 and turnX == 0) or (dirX == 0 and turnY == 0):
                    if grid[x+turnX][y+turnY] != ' ':
                        dirX, dirY = turnX, turnY
                        break
        elif grid[x][y] == '-':
            if y == 0 or y == width-1:
                break
        elif grid[x][y] == '|':
            if x == 0 or x == height:
                break
        else:
            if grid[x][y] == ' ':
                break
            sequence += grid[x][y]
        
    return sequence, steps

if __name__ == '__main__':
    with open('day19/input.txt') as f:
        grid = [list(x) for x in f.readlines()]
    
    sequence, steps = solve(grid)
    print(sequence)
    print(steps)