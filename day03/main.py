import math

def solve1(number):
    a = int(math.sqrt(number))
    if a % 2 == 0:
        a -= 1
    
    for i in range(4):
        k = a**2 + i*(a-1)
        d = abs(k - number)
        if d <= (a-1)//2:
            return (a-1-d)

def solve2(number):
    mem = {}
    mem[(0,0)] = 1
    x,y = 0,0
    directions = [(0,-1), (-1,0), (0,1), (1,0)]
    s = 0
    while mem[(x, y)] <= number:
        x += directions[3][0]
        y += directions[3][1]
        mem[(x, y)] = 0
        s += 2
        for i in range(0,4):
            for j in range(0,s):
                if (i == 0 and j > 0) or i > 0:
                    x += directions[i][0]
                    y += directions[i][1]
                    mem[(x, y)] = 0
                for x_d in range(-1,2):
                    for y_d in range(-1,2):
                        if not(x_d == 0 and y_d == 0):
                            if (x+x_d, y+y_d) in mem:
                                mem[(x, y)] += mem[(x+x_d, y+y_d)]
                print(((x,y), mem[(x, y)]))
                if mem[(x, y)] >= number:
                    return mem[(x, y)]
                
            

if __name__ == '__main__':
    with open('day03/input.txt') as f:
        number = int(f.read().strip())
    ans = solve1(number)
    print(ans)
    ans = solve2(number)
    print(ans)


    