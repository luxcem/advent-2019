def part1(source):
    return sum([int(n/3) - 2 for n in source])

def part2(source):
    def calc_fuel(value):
        fuel = int(value / 3) - 2
        if fuel <= 0:
            return 0
        return fuel + calc_fuel(fuel)
    return sum(map(calc_fuel, source))
