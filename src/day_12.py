import math
from functools import reduce


def lcm(a, b):
    return int(abs(a * b) / math.gcd(int(a), int(b)))


class Moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.dx = 0
        self.dy = 0
        self.dz = 0

    @property
    def pos(self):
        return (self.x, self.y, self.z)

    @property
    def vel(self):
        return (self.dx, self.dy, self.dz)

    def __str__(self):
        spos = "pos=<x={0}, y={1}, z={2}>".format(self.x, self.y, self.z)
        svel = "vel=<x={0}, y={1}, z={2}>".format(self.dx, self.dy, self.dz)

        return "{0}, {1}".format(spos, svel)

    def move(self):
        self.x += self.dx
        self.y += self.dy
        self.z += self.dz

    def pot_energy(self):
        return abs(self.x) + abs(self.y) + abs(self.z)

    def kin_energy(self):
        return abs(self.dx) + abs(self.dy) + abs(self.dz)

    def energy(self):
        return self.pot_energy() * self.kin_energy()

    def __hash__(self):
        return hash((self.x, self.y, self.z, self.dx, self.dy, self.dz))


def sign(a):
    return (a > 0) - (a < 0)


def parse_source(source):
    moons = []
    for line in source.strip().split("\n"):
        pos = [int(x[2:]) for x in line.strip("<>\n").split(", ")]
        moons.append(Moon(*pos))
    return moons


def calc_velocity(moons):
    # velocity
    for moon1 in moons:
        for moon2 in moons:
            if moon1 == moon2:
                continue
            moon1.dx += sign(moon2.x - moon1.x)
            moon1.dy += sign(moon2.y - moon1.y)
            moon1.dz += sign(moon2.z - moon1.z)


def part1(source, steps=10):
    moons = parse_source(source)
    for i in range(steps):
        calc_velocity(moons)
        for moon in moons:
            moon.move()

    return sum(moon.energy() for moon in moons)


def part2(source):
    moons = parse_source(source)
    freq = [0, 0, 0]
    start = [[(m.pos[axis], m.vel[axis]) for m in moons] for axis in range(3)]
    i = 0
    while 0 in freq:
        i += 1
        calc_velocity(moons)
        for moon in moons:
            moon.move()
        for axis in range(3):
            if freq[axis] == 0 and start[axis] == [
                (m.pos[axis], m.vel[axis]) for m in moons
            ]:
                freq[axis] = i
        if i > 231700:
            break
    return reduce(lcm, freq)
