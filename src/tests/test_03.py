import os

from ..utils import Input
from ..day_03 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "03.input"), mapt=None, split=None)


def test_solve_part1():
    assert part1(source.split()) == 1264


def test_solve_part2():
    assert part2(source.split()) == 37390
