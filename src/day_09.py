def get_param(source, param, param_mode, relative_base):
    if param_mode == 0:
        return source[param]
    elif param_mode == 1:
        return param
    elif param_mode == 2:
        return source[param + relative_base]


def set_param(source, param, param_mode, relative_base, value):
    if param_mode == 0 or param_mode == 1:
        source[param] = value
    elif param_mode == 2:
        source[param + relative_base] = value


def parse_code(source, inputs):
    cursor = 0
    opcode = 0
    relative_base = 0
    i = 0
    outputs = []
    while True:
        i += 1
        opcode = source[cursor] % 100
        opcode_line = str(source[cursor]).rjust(5, "0")
        mode1, mode2, mode3 = map(int, opcode_line[-3:-6:-1])
        if opcode == 99:
            break
        elif opcode == 1:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            set_param(source, source[cursor + 3], mode3, relative_base, p1 + p2)
            cursor += 4
        elif opcode == 2:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            set_param(source, source[cursor + 3], mode3, relative_base, p1 * p2)
            cursor += 4
        elif opcode == 3:
            set_param(source, source[cursor + 1], mode1, relative_base, next(inputs))
            cursor += 2
        elif opcode == 4:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            outputs.append(p1)
            cursor += 2
        elif opcode == 5:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            if p1 != 0:
                cursor = p2
            else:
                cursor += 3
        elif opcode == 6:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            if p1 == 0:
                cursor = p2
            else:
                cursor += 3
        elif opcode == 7:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            if p1 < p2:
                set_param(source, source[cursor + 3], mode3, relative_base, 1)
            else:
                set_param(source, source[cursor + 3], mode3, relative_base, 0)
            cursor += 4
        elif opcode == 8:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            p2 = get_param(source, source[cursor + 2], mode2, relative_base)
            if p1 == p2:
                set_param(source, source[cursor + 3], mode3, relative_base, 1)
            else:
                set_param(source, source[cursor + 3], mode3, relative_base, 0)
            cursor += 4
        elif opcode == 9:
            p1 = get_param(source, source[cursor + 1], mode1, relative_base)
            relative_base += p1
            cursor += 2

    return source, outputs


def part1(source, inputs=None):
    code = source + [0] * 10000
    if inputs is None:
        inputs = iter([])
    return parse_code(code, inputs)


def part2(source):
    pass
