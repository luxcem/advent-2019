import itertools
import queue
import threading


def parse_line(line, source):
    i = 100
    opcode = line[0]
    for p in line[1:]:
        if int(opcode / i) % 10:
            yield p
        else:
            yield source[p]
        i *= 10


def parse_code(source, inputs, outputs):
    cursor = 0
    opcode = 0
    i = 0
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
            next_input = yield from inputs()
            source[p1] = next_input
            cursor += 2
        elif opcode == 4:
            (p1,) = parse_line(source[cursor : cursor + 2], source)
            outputs(p1)
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
    return source[0]


def part1(source, phase_seq):
    # inputs = deque()
    # outputs = deque()
    # input_sig = 0
    # for phase_sig in phase_seq:
    #     ret = parse_code(source, inputs, outputs)
    #     input_sig = ret[0]

    # return input_sig
    pass


def run_amp(idx, code, inqueue, outqueue):
    # Output function
    def outthing(x):
        print("Spitting out of amp %d: %d" % (idx, x))
        outqueue.put_nowait(x)

    # Input iterator
    def inthing():
        while True:
            try:
                x = inqueue.get_nowait()
                return x
            except queue.Empty:
                pass
            print("yielding in %d" % (idx,))
            yield ()
            print("back from yield in %d" % (idx,))

    return parse_code(code, inthing, outthing)


def part2(source, phase_seq):
    queues = [queue.Queue() for _ in range(6)]
    for (ique, phase) in zip(queues, phase_seq):
        ique.put(phase)

    # init queue 0:
    queues[0].put(0)
    coroutines = []
    for idx in range(5):
        coroutines.append(run_amp(idx, source, queues[idx], queues[(idx + 1) % 5]))

    for _ in itertools.zip_longest(*coroutines):
        pass
    last_out = queues[0].get_nowait()
    print(last_out)

    # for phase_sig in phase_seq:
    #     ret = parse_code(source, iter([phase_sig, input_sig, 0,0]))
    #     input_sig = ret[0]
    #     print(ret)

    # return input_sig
