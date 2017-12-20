import re

def parse(particle):
    regex = re.compile(r'p=<([\d,-]*)>, v=<([\d,-]*)>, a=<([\d,-]*)>')
    m = regex.match(particle)
    pos = tuple([int(x) for x in m.group(1).split(',')])
    vel = tuple([int(x) for x in m.group(2).split(',')])
    acc = tuple([int(x) for x in m.group(3).split(',')])
    return tuple([pos, vel, acc])

def manhattan(vals):
    return [sum([abs(x) for x in val]) for val in vals]

def solve(particles):
    manhattans = [(idx, manhattan(particle)) for idx, particle in enumerate(particles)]
    manhattans.sort(key=lambda x: (x[1][2], x[1][1], x[1][0]))
    
    return manhattans[0][0]

def solve2(_particles):
    particles = _particles[:]
    for _ in range(100):
        particles = step(particles)
        particles = collide(particles)

    return len(particles)

def step(particles):
    ans = []
    for particle in particles:
        pos = particle[0]
        vel = particle[1]
        acc = particle[2]

        vel = tuple([x + d for x, d in zip(vel, acc)])
        pos = tuple([x + d for x, d in zip(pos, vel)])
        ans.append((pos, vel, acc))
    return ans

def collide(particles):
    unique = {}
    for particle in particles:
        if particle[0] not in unique:
            unique[particle[0]] = [particle]
        else:
            unique[particle[0]].append(particle)
    ans = []
    for key, val in unique.items():
        if len(val) == 1:
            ans.append(val[0])
    return ans

if __name__ == '__main__':
    with open('day20/input.txt') as f:
        particles = [parse(x) for x in f.readlines()]
    
    slowest = solve(particles)
    print(slowest)

    collided = solve2(particles)
    print(collided)