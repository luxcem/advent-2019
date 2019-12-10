import os

from ..utils import Input, Point

from ..day_10 import part1, part2

INPUT_DIRECTORY = os.path.join(
    os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "inputs"
)
source = Input("{}/{}".format(INPUT_DIRECTORY, "10.input"), mapt=None, split=None)


def test_part1_0():
    space = """
....
###.
####
###.""".strip()
    assert part1(space) == (Point(1, 1), 8)


def test_part1_1():
    space = """
.#..#
.....
#####
....#
...##
""".strip()
    assert part1(space) == (Point(3, 4), 8)


def test_part1_2():
    space = """
......#.#.
#..#.#....
..#######.
.#.#.###..
.#..#.....
..#....#.#
#..#....#.
.##.#..###
##...#..#.
.#....####
""".strip()
    assert part1(space) == (Point(5, 8), 33)


def test_part1_3():
    space = """
.#..#..###
####.###.#
....###.#.
..###.##.#
##.##.#.#.
....###..#
..#.#..#.#
#..#.#.###
.##...##.#
.....#.#..""".strip()
    assert part1(space) == (Point(6, 3), 41)


def test_part1_4():
    space = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##""".strip()
    assert part1(space) == (Point(11, 13), 210)


def test_solve_part1():
    assert part1(source) == (Point(23, 20), 334)


def test_part2_1():
    space = """
.#..##.###...#######
##.############..##.
.#.######.########.#
.###.#######.####.#.
#####.##.#.##.###.##
..#####..#.#########
####################
#.####....###.#.#.##
##.#################
#####.##.###..####..
..######..##.#######
####.##.####...##..#
.#####..#.######.###
##...#.##########...
#.##########.#######
.####.#.###.###.#.##
....##.##.###..#####
.#.#.###########.###
#.#.#.#####.####.###
###.##.####.##.#..##
""".strip()
    assert part2(space) == Point(8, 2)


def test_solve_part2():
    assert part2(source) == Point(11, 19)
