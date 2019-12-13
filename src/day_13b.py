import os
import sys
import time

from .intcode import IntCodeComputer
from .utils import Input

INPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
problem = Input("{}/{}".format(INPUT_DIRECTORY, "13.input"), mapt=None, split=None)
code = list(map(int, problem.split(","))) + [0] * 1000


def print_there(x, y, char):
    print("\033[" + str(y) + ";" + str(x) + "H" + char)


def print_screen(grid):
    chars = [" ", "█", "░", "▂", "⬤"]
    miny = min([a[1] for a in grid.keys()])
    maxy = max([a[1] for a in grid.keys()]) + 1
    minx = min([a[0] for a in grid.keys()])
    maxx = max([a[0] for a in grid.keys()]) + 1
    for i in range(miny, maxy):
        for j in range(minx, maxx):
            print_there(j + 3, i + 3, chars[grid[(j, i)]])
    time.sleep(0.01)

class Bot:
    def __init__(self, debug=False):
        self.screen = {}
        self.score = 0
        self.balx = None
        self.padx = None
        self.args = []
        self.debug = debug

    def get_input(self, x, y, value):
        if x == -1 and y == 0:
            self.score = value
            return
        self.screen[(x, y)] = value
        if value == 3:
            self.padx = x
        elif value == 4:
            self.balx = x

    def input(self, value):
        self.args.append(value)
        if len(self.args) == 3:
            self.get_input(*self.args)
            self.args = []

    def output(self):
        if self.debug:
            print_screen(self.screen)
        if self.balx < self.padx:
            return -1
        elif self.balx > self.padx:
            return 1
        return 0


def part2(debug=False):
    source = code.copy()
    source[0] = 2
    bot = Bot(debug)
    computer = IntCodeComputer(source, bot.output, bot.input)
    computer.run()
    return bot.score


if __name__ == "__main__":
    part2(debug=True)
