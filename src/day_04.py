def check_number1(n):
    digits = tuple(map(int, list(str(n))))
    adjacent = False
    for i in [0, 1, 2, 3, 4]:
        if digits[i] == digits[i + 1]:
            adjacent = True
    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False
    return adjacent


def check_number2(n):
    digits = tuple(map(int, list(str(n))))
    adjacent = False
    if digits[0] == digits[1] and digits[0] != digits[2]:
        adjacent = True
    if digits[4] == digits[5] and digits[4] != digits[3]:
        adjacent = True
    for i in [1, 2, 3]:
        if (
            digits[i] == digits[i + 1]
            and digits[i] != digits[i + 2]
            and digits[i] != digits[i - 1]
        ):
            adjacent = True
    for i in range(5):
        if digits[i] > digits[i + 1]:
            return False
    return adjacent


def part1():
    return len(list(filter(check_number1, range(138307, 654504))))


def part2():
    return len(list(filter(check_number2, range(138307, 654504))))
