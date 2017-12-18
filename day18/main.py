from multiprocessing import pool
import multiprocessing

def solve(instructions):
    ans = run(0, instructions, None, None, False)
    return ans

def solve2(instructions):
    queue1 = multiprocessing.Queue()
    queue2 = multiprocessing.Queue()

    lock = False

    threads = pool.ThreadPool(processes=2)
    
    ans1 = threads.apply_async(run, (0, instructions, queue1, queue2, lock))
    ans2 = threads.apply_async(run, (1, instructions, queue2, queue1, lock))

    return ans2.get()


def run(id, instructions, send, recv, lock):
    registers = {}
    registers['p'] = id
    pos = 0
    count = 0

    def value(x):
        try:
            return int(x)
        except ValueError:
            if x in registers:
                return registers[x]
            else:
                return 0

    while True:
        instruction = instructions[pos].strip().split(' ')
        
        if instruction[0] == 'snd':
            freq = value(instruction[1])
            if send:
                send.put(value(instruction[1]))
            count +=1
        if instruction[0] == 'set':
            registers[instruction[1]] = value(instruction[2])
        if instruction[0] == 'add':
            if instruction[1] in registers:
                registers[instruction[1]] += value(instruction[2])
            else:
                registers[instruction[1]] = value(instruction[2])
        if instruction[0] == 'mul':
            if instruction[1] in registers:
                registers[instruction[1]] *= value(instruction[2])
            else:
                registers[instruction[1]] = 0
        if instruction[0] == 'mod':
            if instruction[1] in registers:
                registers[instruction[1]] %= value(instruction[2])
            else:
                registers[instruction[1]] = 0
        if instruction[0] == 'rcv':
            if recv:
                try:
                    recieve = recv.get(block=True, timeout=2)
                except multiprocessing.queues.Empty:
                    return count
                registers[instruction[1]] = recieve
            elif registers[instruction[1]] != 0:
                return freq
        if instruction[0] == 'jgz':
            if value(instruction[1]) > 0:
                pos += value(instruction[2])
            else:
                pos += 1
        else:
            pos += 1
        if pos >= len(instructions):
            break
    return count

if __name__ == '__main__':
    with open('day18/input.txt') as f:
        instructions = f.readlines()
    
    execute = solve(instructions)
    print(execute)

    execute = solve2(instructions)
    print(execute)