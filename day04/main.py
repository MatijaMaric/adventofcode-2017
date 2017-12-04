
def solve(passwords):
    ans = 0
    for password in passwords:
        words = password.split()
        uniques = set(words)
        if len(words) == len(uniques):
            ans += 1
    return ans

def solve2(passwords):
    ans = 0
    for password in passwords:
        words = password.split()
        words = [''.join(sorted(list(x))) for x in words]
        uniques = set(words)
        if len(words) == len(uniques):
            ans += 1
    return ans

if __name__ == '__main__':
    with open('day04/input.txt') as f:
        passwords = f.read().strip().split('\n')

    uniques = solve(passwords)
    print(uniques)

    anagrams = solve2(passwords)
    print(anagrams)