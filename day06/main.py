
def solve(mem):
    memory = mem.split('\t')
    configurations = set()
    idx_conf = {}
    configuration = ' '.join(memory)
    configurations.add(configuration)
    idx_conf[configuration] = 0
    while True:
        idx_max = max(enumerate(memory), key=lambda x:int(x[1]))[0]
        val_max = int(memory[idx_max])
        memory[idx_max] = '0'
        size = len(memory)
        for i in range(1, val_max+1):
            j = (idx_max+i) % size
            memory[j] = str(int(memory[j]) + 1)
        configuration = ' '.join(memory)
        if configuration in configurations:
            length = len(configurations)
            return length - idx_conf[configuration], length
        configurations.add(configuration)
        idx_conf[configuration] = len(configurations)-1

if __name__ == '__main__':
    with open('day06/input.txt') as f:
        mem = f.read().strip()
    
    loop, cycles = solve(mem)
    print(cycles)
    print(loop)