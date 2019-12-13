import os

from ..utils import Input

from ..day_09 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
problem = Input("{}/{}".format(INPUT_DIRECTORY, "09.input"), mapt=None, split=None)


def test_part1():
    code = [104, 1125899906842624, 99]
    outputs = part1(code)
    assert outputs[0] == 1125899906842624
    code = [1102, 34915192, 34915192, 7, 4, 7, 99, 0]
    outputs = part1(code)
    assert outputs[0] == 1219070632396864


def test_part1_2():
    code = [109, 1, 204, -1, 1001, 100, 1, 100, 1008, 100, 16, 101, 1006, 101, 0, 99]
    outputs = part1(code)
    assert outputs == code


def test_solve_part1():
    code = list(map(int, problem.split(",")))
    outputs = part1(code, iter([1]))
    assert outputs[0] == 2752191671
    outputs = part1(code, iter([2]))
    assert outputs[0] == 87571


def test_solve_part2():
    pass
