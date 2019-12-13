import itertools
import queue
import sys
import threading

from .intcode import IntCodeComputer


def run_amp(idx, source, inqueue, outqueue):
    def outthing(x):
        # print("Spitting out of amp %d: %d" % (idx, x))
        outqueue.put_nowait(x)

    def inthing():
        return inqueue.get(True, 2)

    computer = IntCodeComputer(source.copy(), inthing, outthing)
    computer.run()


def part1(source, phase_seq):
    queues = [queue.Queue() for _ in range(6)]
    for (ique, order) in zip(queues, phase_seq):
        ique.put(order)
    queues[0].put(0)
    threads = []
    for idx in range(5):
        threads.append(
            threading.Thread(
                target=run_amp, args=(idx, source, queues[idx], queues[(idx + 1) % 5])
            )
        )
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    return queues[0].get_nowait()
