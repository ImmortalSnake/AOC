import math


def part1():
    maxi, maxp = 0, (0, 0)
    n1, n2 = len(lst), len(lst[0])

    for y1 in range(n1):
        for x1 in range(n2):
            if lst[y1][x1] == '.':
                continue

            lines = []
            for y2 in range(n1):
                for x2 in range(n2):
                    if lst[y2][x2] == '.':
                        continue

                    rad = math.atan2((y2 - y1), (x2 - x1))
                    if rad not in lines:
                        lines.append(rad)

            if len(lines) > maxi:
                maxi, maxp = len(lines), (x1, y1)

    print("Answer 1:", maxi, "at", maxp)


def get_lines(lst, x1, y1):
    n1, n2 = len(lst), len(lst[0])
    lines = []

    for y2 in range(n1):
        for x2 in range(n2):
            if lst[y2][x2] == '.':
                continue

            rad = math.atan2(y2 - y1, x2 - x1)
            # Brings this region up
            if rad < -(math.pi / 2): rad += 2 * math.pi

            if not len([x for x in lines if x[0] == rad]):
                lines.append((rad, x2, y2))

    return lines


def part2():
    x1, y1 = 26, 28
    vap = 0

    while vap < 200:
        lines = sorted(get_lines(lst, x1, y1))

        for r, x, y in lines:
            vap += 1
            if vap == 200:
                break

            lst[y][x] = '.'

    print("Answer 2:", x * 100 + y)


with open("input.txt") as f:
    content = f.read()
    lst = [list(p) for p in content.split('\n')]

part1()
part2()
