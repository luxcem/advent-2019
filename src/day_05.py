def parse_line(line, source):
    i = 100
    opcode = line[0]
    for p in line[1:]:
        if int(opcode / i) % 10:
            yield p
        else:
            yield source[p]
        i *= 10


def parse_code(source, inputs):
    cursor = 0
    opcode = 0
    i = 0
    outputs = []
    while True:
        i += 1
        opcode = source[cursor] % 100
        if opcode == 99:
            break
        elif opcode == 1:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            p3 = source[cursor + 3]
            source[p3] = p1 + p2
            cursor += 4
        elif opcode == 2:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            p3 = source[cursor + 3]
            source[p3] = p1 * p2
            cursor += 4
        elif opcode == 3:
            p1 = source[cursor + 1]
            source[p1] = int(next(inputs))
            cursor += 2
        elif opcode == 4:
            (p1,) = parse_line(source[cursor : cursor + 2], source)
            outputs.append(p1)
            cursor += 2
        elif opcode == 5:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            if p1 != 0:
                cursor = p2
            else:
                cursor += 3
        elif opcode == 6:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            if p1 == 0:
                cursor = p2
            else:
                cursor += 3
        elif opcode == 7:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            p3 = source[cursor + 3]
            if p1 < p2:
                source[p3] = 1
            else:
                source[p3] = 0
            cursor += 4
        elif opcode == 8:
            p1, p2 = parse_line(source[cursor : cursor + 3], source)
            p3 = source[cursor + 3]
            if p1 == p2:
                source[p3] = 1
            else:
                source[p3] = 0
            cursor += 4

    return outputs


def part1(source, inputs):
    return parse_code(source, inputs)


def part2(source):
    pass
