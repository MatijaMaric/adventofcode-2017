
def solve(numbers, iter, picky):
    a = numbers[0]
    b = numbers[1]
    ans = 0

    for _ in range(iter):
        if same(a, b):
            ans += 1
        while True:
            a = (a*16807) % 2147483647
            if a % 4 == 0 or not picky:
                break
        while True:
            b = (b*48271) % 2147483647
            if b % 8 == 0 or not picky:
                break

    return ans

def same(a, b):
    bot_a = a & 0b1111111111111111
    bot_b = b & 0b1111111111111111

    return bot_a == bot_b

if __name__ == '__main__':
    with open('day15/input.txt') as f:
        numbers = [int(x.split(' ')[-1]) for x in f.readlines()]
    
    pairs = solve(numbers, 4*10**7, False)
    print(pairs)

    pairs2 = solve(numbers, 5*10**6, True)
    print(pairs2)