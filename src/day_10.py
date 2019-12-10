import operator
from math import acos
import numpy as np
from .utils import Point


def read_source(source):
    source = source.split()
    h = len(source)
    w = len(source[0])
    asteroids = []
    for (y, line) in enumerate(source):
        for (x, value) in enumerate(line):
            if value == "#":
                asteroids.append(Point(x, y))
    return {"h": h, "w": w, "asteroids": asteroids}


def push(d, key, value):
    if key in d:
        d[key].append(value)
    else:
        d[key] = [value]


def calc_fov(asteroids):
    output = {}
    for asteroid in asteroids:
        directions = {}
        for other in asteroids:
            if other == asteroid:
                continue
            direction = other - asteroid
            dot = Point(0, -1) * direction.norm()
            angle = acos(dot)
            if other.x < asteroid.x:
                angle = np.pi * 2 - angle
            angle = round(angle, 4)
            push(directions, angle, other)
        output[asteroid] = directions
    return output


def part1(source):
    problem = read_source(source)
    outputs = calc_fov(problem["asteroids"])
    max_fov = {}
    for asteroid in outputs:
        max_fov[asteroid] = len(outputs[asteroid])

    return max(max_fov.items(), key=operator.itemgetter(1))


def closest(start, l):
    def distance(point):
        return (point - start).length_sq()

    return min(l, key=distance)


def part2(source):
    problem = read_source(source)
    outputs = calc_fov(problem["asteroids"])
    max_fov = {}
    for asteroid in outputs:
        max_fov[asteroid] = len(outputs[asteroid])
    station = max(max_fov.items(), key=operator.itemgetter(1))[0]

    asteroid_fov = outputs[station]
    directions = sorted(list(asteroid_fov.keys()))

    keep_going = True
    i = 1
    while i < 200:
        for direction in directions:
            targets = asteroid_fov[direction]
            if targets == []:
                continue
            close = closest(station, targets)
            asteroid_fov[direction].remove(close)
            # print("The {}th asteroid to be vaporized is at {}".format(i, close))
            if i == 200:
                return close
            i += 1
