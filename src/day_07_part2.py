import sys
import itertools
import queue
import threading


def get_param(prog, idx, param_num):
    imode = prog[idx] // (10 * 10 ** param_num)
    val = prog[idx + param_num]
    if imode % 10 == 0:
        return prog[val]
    if imode % 10 == 1:
        return val
    print("BAD get imode %d at idx %d" % (imode, idx))
    sys.exit(2)


def set_param(prog, idx, param_num, set_to):
    imode = prog[idx] // (10 * 10 ** param_num)
    val = prog[idx + param_num]
    if imode % 10 == 0:
        prog[val] = set_to
        return
    print("BAD set imode %d at idx %d" % (imode, idx))
    sys.exit(2)


def evalprog(amp_num, iprog, inputf, outputf):
    prog = list(iprog)
    idx = 0
    while True:
        if prog[idx] % 100 == 1:
            p1 = get_param(prog, idx, 1)
            p2 = get_param(prog, idx, 2)
            set_param(prog, idx, 3, get_param(prog, idx, 1) + get_param(prog, idx, 2))
            idx += 4
        elif prog[idx] % 100 == 2:
            set_param(prog, idx, 3, get_param(prog, idx, 1) * get_param(prog, idx, 2))
            idx += 4
        elif prog[idx] % 100 == 3:
            x = inputf()
            set_param(prog, idx, 1, x)
            idx += 2
        elif prog[idx] % 100 == 4:
            outputf(get_param(prog, idx, 1))
            idx += 2
        elif prog[idx] % 100 == 5:
            p1 = get_param(prog, idx, 1)
            if p1:
                idx = get_param(prog, idx, 2)
            else:
                idx += 3
        elif prog[idx] % 100 == 6:
            p1 = get_param(prog, idx, 1)
            if not p1:
                idx = get_param(prog, idx, 2)
            else:
                idx += 3
        elif prog[idx] % 100 == 7:
            p1 = get_param(prog, idx, 1)
            p2 = get_param(prog, idx, 2)
            set_param(prog, idx, 3, 1 if p1 < p2 else 0)
            idx += 4
        elif prog[idx] % 100 == 8:
            p1 = get_param(prog, idx, 1)
            p2 = get_param(prog, idx, 2)
            set_param(prog, idx, 3, 1 if p1 == p2 else 0)
            idx += 4
        elif prog[idx] % 100 == 99:
            idx += 1
            break
        else:
            print("BAD CODE %d AT %d" % (prog[idx], idx))
            sys.exit(2)
    return prog[0]


def run_amp(idx, prog, inqueue, outqueue):
    def outthing(x):
        # print("Spitting out of amp %d: %d" % (idx, x))
        outqueue.put_nowait(x)

    evalprog(idx, prog, lambda: inqueue.get(True, 2), outthing)


def part2(data, phase_seq):
    prog = data
    max_output = -1000

    queues = [queue.Queue() for _ in range(6)]
    for (ique, order) in zip(queues, phase_seq):
        ique.put(order)
    queues[0].put(0)
    threads = []
    for idx in range(5):
        threads.append(
            threading.Thread(
                target=run_amp, args=(idx, prog, queues[idx], queues[(idx + 1) % 5])
            )
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    last_out = queues[0].get_nowait()
    max_output = max(max_output, last_out)

    return max_output
