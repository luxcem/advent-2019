import os
from itertools import permutations

from ..utils import Input

from ..day_07 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "07.input"), mapt=None, split=None)


def test1_part1():
    code = [3, 15, 3, 16, 1002, 16, 10, 16, 1, 16, 15, 15, 4, 15, 99, 0, 0]
    phase_seq = [4, 3, 2, 1, 0]
    assert part1(code, phase_seq) == 43210


def test2_part1():
    code1 = [3, 23, 3, 24, 1002, 24, 10, 24, 1002, 23]
    code2 = [-1, 23, 101, 5, 23, 23, 1, 24, 23, 23, 4, 23, 99, 0, 0]
    code = code1 + code2
    phase_seq = [0, 1, 2, 3, 4]
    assert part1(code, phase_seq) == 54321


def test3_part1():
    code1 = [3, 31, 3, 32, 1002, 32, 10, 32, 1001, 31, -2, 31, 1007, 31, 0, 33]
    code2 = [1002, 33, 7, 33, 1, 33, 31, 31, 1, 32, 31, 31, 4, 31, 99, 0, 0, 0]
    code = code1 + code2
    phase_seq = [1, 0, 4, 3, 2]
    assert part1(code, phase_seq) == 65210


def test_solve_part1():
    code = list(map(int, source.split(",")))

    max_output = 0
    for phase_seq in permutations([0, 1, 2, 3, 4], 5):
        output = part1(code, phase_seq)
        max_output = max(max_output, output)
    assert max_output == 99376


def test_part2():
    code1 = [3, 26, 1001, 26, -4, 26, 3, 27, 1002, 27, 2, 27, 1, 27, 26]
    code2 = [27, 4, 27, 1001, 28, -1, 28, 1005, 28, 6, 99, 0, 0, 5]
    code = code1 + code2
    phase_seq = [9, 8, 7, 6, 5]
    output = part2(code, phase_seq)
    print(output)


def test_solve_part2():
    pass
