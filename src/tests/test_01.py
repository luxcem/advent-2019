import os

from ..utils import Input
from ..day_01 import part1, part2

INPUT_DIRECTORY = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs")
source = Input("{}/{}".format(INPUT_DIRECTORY, "01.input"))

def test_part1():
    assert part1([12]) == 2
    assert part1([14]) == 2
    assert part1([1969]) == 654
    assert part1([100756]) == 33583

def test_solve_part1():
    assert part1(source) == 3216868

def test_part2():
    assert part2([1969]) == 966
    assert part2([100756]) == 50346

def test_solve_part2():
    assert part2(source) == 4822435
