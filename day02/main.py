
def solve(file_lines):
    sum = 0

    for line in file_lines:
        line = line.strip()
        numbers = line.split('\t')
        max_num = float('-inf')
        min_num = float('inf')
        for number in numbers:
            parse = int(number)
            if parse < min_num:
                min_num = parse
            if parse > max_num:
                max_num = parse
        
        sum += max_num - min_num
    
    return sum

def solve2(file_lines):
    sum = 0

    for line in file_lines:
        line = line.strip()
        numbers = [int(x) for x in line.split('\t')]
        for i, number1 in enumerate(numbers):
            for j, number2 in enumerate(numbers):
                if i != j:
                    if number1 % number2 == 0:
                        sum += number1 / number2
                        break
    
    return sum

if __name__ == '__main__':
    with open('day02/input.txt') as f:
        file_lines = f.readlines()

    checksum = solve(file_lines)
    print(checksum)

    divisibles = solve2(file_lines)
    print(divisibles)