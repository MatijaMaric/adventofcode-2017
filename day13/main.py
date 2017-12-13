
def passthrough(firewall, delay, stop):
    caught = 0
    for depth, range in firewall:
        if scan(range, depth+delay) == 0:
            if stop:
                return 1
            caught += depth*range
    
    return caught

def safepass(firewall):
    delay = 0
    while passthrough(firewall, delay, True) > 0:
        delay += 1
    return delay

def scan(range, time):
    pos = time % (2*range - 2)
    return pos

if __name__ == '__main__':
    with open('day13/input.txt') as f:
        firewall = [tuple([int(y) for y in x.split(':')]) for x in f.readlines()]

    caught = passthrough(firewall, 0, False)
    print(caught)

    delay = safepass(firewall)
    print(delay)