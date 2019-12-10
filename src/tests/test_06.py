import os

from ..utils import Input

from ..day_06 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "06.input"), mapt=None, split=None)


def test_part1():
    test_input = """
    COM)B
    B)C
    C)D
    D)E
    E)F
    B)G
    G)H
    D)I
    E)J
    J)K
    K)L
    K)YOU
    I)SAN
    """.split()
    assert part1(test_input) == 54


def test_solve_part1():
    assert part1(source.split()) == 245089


def test_solve_part2():
    assert part2(source.split()) == 511
