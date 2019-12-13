import os

from ..utils import Input

from ..day_12 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "12.input"), mapt=None, split=None)


def test_part1():
    test_source = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""
    assert part1(test_source, 10) == 179


def test2_part1():
    test_source = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""
    assert part1(test_source, 100) == 1940


def test_solve_part1():
    assert part1(source, 1000) == 7098


def test_part2():
    test_source = """
<x=-1, y=0, z=2>
<x=2, y=-10, z=-7>
<x=4, y=-8, z=8>
<x=3, y=5, z=-1>
"""
    assert part2(test_source) == 2772


def test2_part2():
    test_source = """
<x=-8, y=-10, z=0>
<x=5, y=5, z=10>
<x=2, y=-7, z=3>
<x=9, y=-8, z=-3>
"""
    pass
    # assert part2(test_source) == 4686774924


def test_solve_part2():
    assert part2(source) == 400128139852752
