
def solve(lengths):
    numbers = list(range(256))
    numbers = knot(numbers, lengths, 1)
    
    return numbers[0] * numbers[1]

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

if __name__ == '__main__':
    with open('day10/input.txt') as f:
        string = f.read().strip()
        lengths = [int(x) for x in string.split(',')] 

    mult = solve(lengths)
    print(mult)

    knot = knot_hash(string)
    print(knot)