import os

from queue import Queue, Empty
from threading import Thread


from .intcode import IntCodeComputer
from .utils import Input

INPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
problem = Input("{}/{}".format(INPUT_DIRECTORY, "13.input"), mapt=None, split=None)
code = list(map(int, problem.split(","))) + [0] * 1000


def print_screen(grid):
    chars = [" ", "█", "░", "▂", "⬤"]
    miny = min([a[1] for a in grid.keys()])
    maxy = max([a[1] for a in grid.keys()]) + 1
    minx = min([a[0] for a in grid.keys()])
    maxx = max([a[0] for a in grid.keys()]) + 1
    print()
    print("---")
    for i in range(miny, maxy):
        for j in range(minx, maxx):
            print(chars[grid[(j, i)]], end="")
        print()
    print("---")


def robot(inqueue, outqueue, rqueue):
    screen = {}
    while True:
        try:
            x = inqueue.get(True, 0.05)
            y = inqueue.get(True, 0.05)
            tile = inqueue.get(True, 0.05)
            screen[(x, y)] = tile
        except Empty:
            break
    result = len(list(filter(lambda x: x == 2, screen.values())))
    rqueue.put_nowait(result)


def robot2(inqueue, outqueue, rqueue):
    screen = {}
    score = None
    ball_pos = None
    pad_pos = None
    while True:
        try:
            x = inqueue.get(True, 0.001)
            y = inqueue.get()
            tile = inqueue.get()
        except Empty:
            if not outqueue.empty():
                break
            if ball_pos is not None and pad_pos is not None and score is not None:
                print_screen(screen)
                print(score)
                # print("Ball {}, Pad {}".format(ball_pos, pad_pos))
                play = 0
                if ball_pos < pad_pos:
                    play = -1
                elif ball_pos > pad_pos:
                    play = 1
                # print("Play {}".format(play))
                outqueue.put_nowait(play)

        if x == -1 and y == 0:
            score = tile
        else:
            screen[(x, y)] = tile
            if tile == 4:
                # ball position
                ball_pos = x
            elif tile == 3:
                pad_pos = x

    rqueue.put_nowait(score)


def run_code(code, inqueue, outqueue):
    def outthing(x):
        # print("Brain out {}".format(x))
        outqueue.put_nowait(x)

    def inthing():
        # print("Brain waiting for instructions...")
        x = inqueue.get()
        while not inqueue.empty():
            x = inqueue.get()
        # print("Brain received {}".format(x))
        return x

    computer = IntCodeComputer(code.copy(), inthing, outthing)
    computer.run()


def part1():
    print()
    a_queue = Queue()
    b_queue = Queue()
    r_queue = Queue()
    robot_thread = Thread(target=robot, args=(b_queue, a_queue, r_queue))
    computer_thread = Thread(target=run_code, args=(code, a_queue, b_queue))
    robot_thread.start()
    computer_thread.start()

    robot_thread.join()
    computer_thread.join()
    return r_queue.get()


def part2():
    source = code.copy()
    source[0] = 2
    a_queue = Queue()
    b_queue = Queue()
    r_queue = Queue()
    robot_thread = Thread(target=robot2, args=(b_queue, a_queue, r_queue))
    computer_thread = Thread(target=run_code, args=(source, a_queue, b_queue))
    robot_thread.start()
    computer_thread.start()

    robot_thread.join()
    computer_thread.join()
    return r_queue.get()
