from collections import deque

def knot(numbers, lengths, times):
    pos = 0
    skip = 0
    for _ in range(times):
        for length in lengths:
            revert(numbers, pos, length)
            pos += length + skip
            skip += 1
    return numbers

def revert(numbers, pos, length):
    temp = []
    len_numbers = len(numbers)
    for i in range(length):
        temp.append(numbers[(pos+i) % len_numbers])
    for i in range(length):
        numbers[(pos+length-i-1) % len_numbers] = temp[i]    
    return numbers

def dense(numbers):
    ans = []
    for i in range(16):
        xor = 0
        for j in range(i*16,i*16+16):
            xor ^= numbers[j]
        ans.append(xor)
    return ans

def knot_hash(string):
    numbers = [ord(x) for x in list(string)]
    salt = [17, 31, 73, 47, 23]
    numbers += salt
    hashed = dense(knot(list(range(256)), numbers, 64))
    return ''.join(f'{i:02x}' for i in hashed)

def count_regions(grid):
    visited = set()
    q = deque()
    moves = [(-1, 0), (0, -1), (1, 0), (0, 1)]
    ans = 0
    for i in range(128):
        for j in range(128):
            if grid[i][j] == 1 and (i, j) not in visited:
                ans += 1
                visited.add((i, j))
                q.append((i, j))
                while len(q) > 0:
                    x, y = q.pop()
                    for dx, dy in moves:
                        m, n = x+dx, y+dy
                        if m >= 0 and m < 128 and n >= 0 and n < 128:
                            if grid[m][n] == 1:
                                if (m, n) not in visited:
                                    visited.add((m, n))
                                    q.append((m, n))
    return ans

def solve(key):
    ans = 0
    grid = []

    for i in range(128):
        string = key + '-' + str(i)
        hashed = knot_hash(string)
        binary_str = bin(int(hashed, 16))[2:]
        binary_str = binary_str.zfill(128)
        binary = [int(d) for d in list(binary_str)]
        
        ans += sum(binary)

        grid.append(binary)
    return ans, count_regions(grid)

if __name__ == '__main__':
    with open('day14/input.txt') as f:
        key = f.read().strip()
    
    used, regions = solve(key)
    print(used)
    print(regions)