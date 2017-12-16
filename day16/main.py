
def dance(pos, moves):
    if pos == None:
        programs = [chr(x) for x in range(ord('a'), ord('p')+1)]
    else:
        programs = pos
    
    for move in moves:
        if move[0] == 's':
            spins = int(move[1:])
            programs = programs[-spins:] + programs[:-spins]
        if move[0] == 'x':
            tmp = [int(x) for x in move[1:].split('/')]
            idx1 = tmp[0]
            idx2 = tmp[1]
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]
        if move[0] == 'p':
            prog1 = move[1]
            prog2 = move[3]
            idx1 = programs.index(prog1)
            idx2 = programs.index(prog2)
            programs[idx1], programs[idx2] = programs[idx2], programs[idx1]

    return programs

def repeat(pos, moves, times):
    programs = list(pos)
    permutes = []
    shuffle = [ord(x) - ord('a') for x in list(programs)]
    joined = pos
    while joined not in permutes:
        permutes.append(joined)
        programs = dance(programs, moves)
        joined = ''.join(programs)
    return permutes[times % len(permutes)]

if __name__ == '__main__':
    with open('day16/input.txt') as f:
        moves = f.read().split(',')
    
    one = ''.join(dance(None, moves))
    print(one)
    
    billion = ''.join(repeat(one, moves, 10**9 - 1))
    print(billion)
