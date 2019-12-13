import sys


class IntCodeComputer:
    def __init__(self, source, inputf, outputf):
        self.source = source
        self.inputf = inputf
        self.outputf = outputf
        self.rel_base = 0

    def get(self, param, param_mode):
        if param_mode == 0:
            return self.source[param]
        elif param_mode == 1:
            return param
        elif param_mode == 2:
            return self.source[param + self.rel_base]

    def set(self, param, param_mode, value):
        if param_mode == 0 or param_mode == 1:
            self.source[param] = value
        elif param_mode == 2:
            self.source[param + self.rel_base] = value

    def run(self):
        cursor = 0
        opcode = 0
        i = 0
        while True:
            i += 1
            opcode = self.source[cursor] % 100
            opcode_line = str(self.source[cursor]).rjust(5, "0")
            mode1, mode2, mode3 = map(int, opcode_line[-3:-6:-1])
            if opcode == 1:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                self.set(self.source[cursor + 3], mode3, p1 + p2)
                cursor += 4
            elif opcode == 2:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                self.set(self.source[cursor + 3], mode3, p1 * p2)
                cursor += 4
            elif opcode == 3:
                x = self.inputf()
                self.set(self.source[cursor + 1], mode1, x)
                cursor += 2
            elif opcode == 4:
                p1 = self.get(self.source[cursor + 1], mode1)
                self.outputf(p1)
                cursor += 2
            elif opcode == 5:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                if p1 != 0:
                    cursor = p2
                else:
                    cursor += 3
            elif opcode == 6:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                if p1 == 0:
                    cursor = p2
                else:
                    cursor += 3
            elif opcode == 7:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                self.set(self.source[cursor + 3], mode3, 1 if p1 < p2 else 0)
                cursor += 4
            elif opcode == 8:
                p1 = self.get(self.source[cursor + 1], mode1)
                p2 = self.get(self.source[cursor + 2], mode2)
                self.set(self.source[cursor + 3], mode3, 1 if p1 == p2 else 0)
                cursor += 4
            elif opcode == 9:
                p1 = self.get(self.source[cursor + 1], mode1)
                self.rel_base += p1
                cursor += 2
            elif opcode == 99:
                break
            else:
                print("BAD CODE %d AT %d" % (self.source[cursor], cursor))
                sys.exit(2)

        return self.source
