import os

from ..utils import Input
from ..day_02 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "02.input"), mapt=None, split=None)


def test_part1():
    expected = [3500, 9, 10, 70, 2, 3, 11, 0, 99, 30, 40, 50]
    assert part1("1,9,10,3,2,3,11,0,99,30,40,50") == expected
    assert part1("1,0,0,0,99") == [2, 0, 0, 0, 99]
    assert part1("2,3,0,3,99") == [2, 3, 0, 6, 99]
    assert part1("2,4,4,5,99,0") == [2, 4, 4, 5, 99, 9801]
    assert part1("1,1,1,4,99,5,6,0,99") == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_solve_part1():
    code = source.split(",")
    code[1] = "12"
    code[2] = "2"
    code = ",".join(code)
    assert part1(code)[0] == 4945026


def test_solve_part2():
    code = list(map(int, source.split(",")))
    assert part2(code) == 5296
