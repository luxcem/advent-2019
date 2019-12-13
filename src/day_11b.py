import os

from .intcode import IntCodeComputer
from .utils import Input

INPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.abspath(__file__)), "inputs")
problem = Input("{}/{}".format(INPUT_DIRECTORY, "11.input"), mapt=None, split=None)
code = list(map(int, problem.split(","))) + [0] * 1000


def print_grid(grid, x=0, y=0, facing=0):
    facing_list = ["^", ">", "v", "<"]
    miny = min([a[1] for a in grid.keys()])
    maxy = max([a[1] for a in grid.keys()]) + 1
    minx = min([a[0] for a in grid.keys()])
    maxx = max([a[0] for a in grid.keys()]) + 1

    for i in range(miny, maxy):
        for j in range(minx, maxx):
            if not (j, i) in grid:
                print(".", end="")
            elif (i, j) == (y, x):
                print(facing_list[facing], end="")
            else:
                print("#" if grid[(j, i)] else ".", end="")
        print()


class Bot:
    def __init__(self, start, debug=False):
        self.grid = {(0, 0): start}
        self.x = 0
        self.y = 0
        self.dx = 0
        self.dy = -1
        self.args = []

    def get_input(self, color, move):
        # Action after all input

        self.grid[(self.x, self.y)] = color
        if move:
            self.dx, self.dy = -self.dy, self.dx
        else:
            self.dx, self.dy = self.dy, -self.dx

        self.x += self.dx
        self.y += self.dy

    def input(self, value):
        # read a value
        self.args.append(value)
        if len(self.args) == 2:
            self.get_input(*self.args)
            self.args = []

    def output(self):
        return self.grid.get((self.x, self.y), 0)


def part1(debug=False):
    bot = Bot(0, debug)
    computer = IntCodeComputer(code, bot.output, bot.input)
    computer.run()
    return len(bot.grid)


def part2(debug=False):
    bot = Bot(1, debug)
    computer = IntCodeComputer(code, bot.output, bot.input)
    computer.run()
    print()
    print_grid(bot.grid)
