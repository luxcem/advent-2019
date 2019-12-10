from .utils import Point

directions = {"R": Point(1, 0), "L": Point(-1, 0), "U": Point(0, 1), "D": Point(0, -1)}


def get_intersections(source):
    crossed = {}
    intersections = {}
    coord = Point(0, 0)
    steps = 0
    for instruction in source[0].split(","):
        d, l = instruction[0], int(instruction[1:])
        for _ in range(l):
            steps += 1
            coord += directions[d]
            if coord not in crossed:
                crossed[coord] = steps

    steps = 0
    coord = Point(0, 0)
    for instruction in source[1].split(","):
        d, l = instruction[0], int(instruction[1:])
        for _ in range(l):
            steps += 1
            coord += directions[d]
            if coord in crossed and coord not in intersections:
                intersections[coord] = crossed[coord] + steps
            elif coord in crossed and coord in intersections:
                intersections[coord] = min(intersections[coord], crossed[coord] + steps)
    return intersections


def part1(source):
    intersections = get_intersections(source)
    minimum = Point(100000, 100000)
    for point in intersections.keys():
        if point.x + point.y < minimum.x + minimum.y:
            minimum = point
    return point.x + point.y


def part2(source):
    intersections = get_intersections(source)
    return min(intersections.values())
