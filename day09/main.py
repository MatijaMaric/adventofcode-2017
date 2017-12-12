import re

def solve(stream):
    escapeless = re.sub(r'(!.)', '', stream)
    garbagex = re.compile(r"(<[^>]*>)")
    garbageless = garbagex.sub('', escapeless)
    garbage_len = sum([len(garbage)-2 for garbage in garbagex.findall(escapeless)])
    return score(garbageless), garbage_len

def score(groups):
    ans = 0
    mult = 0
    for char in list(groups):
        if char == '{':
            mult += 1
        elif char == '}':
            ans += mult
            mult -= 1
    return ans
    
if __name__ == '__main__':
    with open('day09/input.txt') as f:
        stream = f.read().strip()
    
    score, garbage_len = solve(stream)
    print(score)
    print(garbage_len)