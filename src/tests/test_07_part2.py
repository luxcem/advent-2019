import os
from itertools import permutations

from ..utils import Input

from ..day_07_part2 import part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "07.input"), mapt=None, split=None)

"""
def test_part2():
    code = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
    phase_seq = [9,8,7,6,5]
    output = part2(code, phase_seq)
    print(output)


def test_solve_part2():
    code = list(map(int, source.split(",")))
    assert part2(code) == 0
"""
