from itertools import product

def parse_code(source):
    cursor = 0
    opcode = 0
    while True:
        opcode = source[cursor]
        if opcode == 99:
            break
        p1, p2, pr = source[cursor + 1 : cursor + 4]
        if opcode == 1:
            source[pr] = source[p1] + source[p2]
        elif opcode == 2:
            source[pr] = source[p1] * source[p2]
        cursor += 4
    return source


def part1(source):
    intcode = list(map(int, source.split(",")))
    return parse_code(intcode)


def part2(source):
    for noun, verb in product(range(100), range(100)):
        new_source = source.copy()
        new_source[1] = noun
        new_source[2] = verb
        if parse_code(new_source.copy())[0] == 19690720:
            return int("{}{}".format(noun, verb))
