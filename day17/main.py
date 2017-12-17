from numba import jit

@jit
def spinlock(steps):
    buffer = [0]
    pos = 0
    for x in range(1, 2018):
        pos = (pos + steps) % x
        buffer.insert(pos+1, x)
        pos += 1
    return buffer[(pos+1)%2018]

@jit
def spinlock_angry(steps):
    cur = 0
    pos = 0
    for x in range(1, 50*10**6):
        pos = (pos + steps) % x
        if pos == 0:
            cur = x
        pos += 1
    return cur

if __name__ == '__main__':
    with open('day17/input.txt') as f:
        steps = int(f.read())
    
    ans = spinlock(steps)
    print(ans)

    angry = spinlock_angry(steps)
    print(angry)