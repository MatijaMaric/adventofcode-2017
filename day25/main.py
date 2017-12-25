from collections import defaultdict

def A(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        return B, tape, pos
    else:
        tape[pos] = 0
        pos += 1
        return C, tape, pos

def B(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 0
        pos -= 1
        return A, tape, pos
    else:
        tape[pos] = 0
        pos += 1
        return D, tape, pos

def C(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        return D, tape, pos
    else:
        tape[pos] = 1
        pos += 1
        return A, tape, pos

def D(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos -= 1
        return E, tape, pos
    else:
        tape[pos] = 0
        pos -= 1
        return D, tape, pos

def E(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        return F, tape, pos
    else:
        tape[pos] = 1
        pos -= 1
        return B, tape, pos

def F(tape, pos):
    if tape[pos] == 0:
        tape[pos] = 1
        pos += 1
        return A, tape, pos
    else:
        tape[pos] = 1
        pos += 1
        return E, tape, pos

def turing(start, steps):
    tape = defaultdict(lambda : 0)
    pos = 0
    current = start
    for _ in range(steps):
        current, tape, pos = current(tape, pos)
    
    return sum(tape.values())

if __name__ == '__main__':
    steps = 12368930
    start = A

    checksum = turing(start, steps)
    print(checksum)

