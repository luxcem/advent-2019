from .intcode import IntCodeComputer


def run_code(code, inputs):
    outputs = []

    def outthing(x):
        outputs.append(x)

    def inthing():
        return next(inputs)

    computer = IntCodeComputer(code.copy(), inthing, outthing)
    computer.run()
    return outputs


def part1(source, inputs=None):
    code = source + [0] * 10000
    if inputs is None:
        inputs = iter([])
    return run_code(code, inputs)


def part2(source):
    pass
