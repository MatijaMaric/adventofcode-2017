def solve_first(captcha):
    ans = 0
    length = len(captcha)
    for i in range(length):
        a = int(captcha[i])
        b = int(captcha[(i+1) % length])
        if a == b:
            ans += a
    return ans

def solve_second(captcha):
    ans = 0
    length = len(captcha)
    for i in range(length):
        a = int(captcha[i])
        b = int(captcha[(i+length//2) % length])
        if a == b:
            ans += a
    return ans

if __name__ == '__main__':
    with open('day01/input.txt') as f:
        captcha = f.read()
    sum = solve_first(list(captcha)[:-1])
    print(sum)
    sum = solve_second(list(captcha)[:-1])
    print(sum)