import os

from queue import Queue, Empty
from threading import Thread


from .intcode import IntCodeComputer
from .utils import Input

INPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
problem = Input("{}/{}".format(INPUT_DIRECTORY, "11.input"), mapt=None, split=None)
code = list(map(int, problem.split(","))) + [0] * 1000



def robot(inqueue, outqueue):
    grid = {(0, 0): 1}
    x, y = 0, 0
    dx, dy = 0, -1
    move_list = ["<", ">"]
    color_list = ["black", "white"]
    while True:
        # for i in range(15):
        current = grid.get((x, y), 0)
        outqueue.put_nowait(current)
        try:
            color = inqueue.get(True, 0.5)
        except Empty:
            break
        move = inqueue.get()
        grid[(x, y)] = color

        # print("Robot received {}, {}".format(move_list[move], color_list[color]))

        if move == 0:
            # turn left
            dx, dy = dy, -dx
        else:
            # turn right
            dx, dy = -dy, dx
        x += dx
        y += dy

    print(len(grid))


def run_code(code, inqueue, outqueue):
    def outthing(x):
        # print("Brain out {}".format(x))
        outqueue.put_nowait(x)

    def inthing():
        # print("Brain waiting for instructions...")
        x = inqueue.get()
        # print("Brain received {}".format(x))
        return x

    computer = IntCodeComputer(code.copy(), inthing, outthing)
    computer.run()


def part1():
    print()
    a_queue = Queue()
    b_queue = Queue()
    robot_thread = Thread(target=robot, args=(b_queue, a_queue))
    computer_thread = Thread(target=run_code, args=(code, a_queue, b_queue))
    robot_thread.start()
    computer_thread.start()

    robot_thread.join()
    computer_thread.join()
