def run(intops, pid=0):
    num_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]
    out = []
    ip = rb = 0

    while intops[ip] != 99:
        modes = [intops[ip] // (10 ** x) % 10 for x in range(2, 5)]
        op = intops[ip] % 100

        operands = [intops[ip + x + 1] if modes[x] == 1 else intops[(rb if modes[x] == 2 else 0) + intops[ip + x + 1]]
                    for x in range(num_operands[op])]

        if op == 1 or op == 2:
            intops[(rb if modes[2] == 2 else 0) + intops[ip + 3]] = operands[0] + operands[1] if op == 1 else operands[0] * operands[1]

        elif op == 3:
            des = (rb if modes[0] == 2 else 0) + intops[ip + 1]
            intops[des] = inputs[pid]

        elif op == 4:
            yield operands[0]

        elif op == 5 or op == 6:
            if (op == 5 and operands[0] != 0) or (op == 6 and operands[0] == 0):
                ip = operands[1] - 3

        elif op == 7 or op == 8:
            if (op == 7 and operands[0] < operands[1]) or (op == 8 and operands[0] == operands[1]):
                intops[(rb if modes[2] == 2 else 0) + intops[ip + 3]] = 1
            else:
                intops[(rb if modes[2] == 2 else 0) + intops[ip + 3]] = 0

        elif op == 9:
            rb += operands[0]
        else:
            assert False

        ip += num_operands[op] + 1

    return intops[0], out


def paint(start=0):
    global inputs
    inputs = [start]
    grid = {(0, 0): start}

    direction = 0
    x, y = 0, 0

    p = run(intcode[:], 0)

    try:
        while True:
            grid[x, y] = next(p)
            direction += 1 if next(p) == 0 else -1
            direction %= 4

            if direction == 0:
                y += 1
            elif direction == 1:
                x += 1
            elif direction == 2:
                y -= 1
            elif direction == 3:
                x -= 1

            inputs[0] = grid.get((x, y), 0)
    except StopIteration:
        return grid


def part2():
    grid = paint(1)
    maxy, maxx = max([x[1] for x in grid.keys()]), max([x[0] for x in grid.keys()])
    miny, minx = min([x[1] for x in grid.keys()]), min([x[0] for x in grid.keys()])

    for y in range(maxy, miny - 1, -1):
        for x in range(maxx, minx + 1, -1):
            if (x, y) in grid and grid[(x, y)] == 1:
                print('#', end="")
            else:
                print(' ', end="")
        print()


with open("input.txt") as f:
    intcode = [int(x) for x in f.read().split(',')] + [0] * 1000

inputs = [0]

print("Part 1:", len(paint(0).keys()))
print("Part 2:")
part2()
