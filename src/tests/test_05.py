import os

from ..utils import Input

from ..day_05 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "05.input"), mapt=None, split=None)


def test_solve_part1():
    code = list(map(int, source.split(",")))
    outputs = part1(code, iter([1]))
    assert outputs[-1] == 6069343


def test_solve_part2():
    code = list(map(int, source.split(",")))
    outputs = part1(code, iter([5]))
    assert outputs[-1] == 3188550
