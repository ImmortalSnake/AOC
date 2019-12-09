def get_children(child, parent):
    p = parent.get(child)

    if not p:
        return []

    return [p] + get_children(p, parent)


def part1(tree):
    print(sum([len(o) for o in tree.values()]))


def part2(tree):
    common = [e for e in tree["YOU"] if e in tree["SAN"]][0]
    print(tree["YOU"].index(common) + tree["SAN"].index(common))


orbits = {}
full = {}

with open("input.txt") as f:
    for l in f.read().splitlines():
        p2, p1 = l.split(')')
        orbits[p1] = p2

for obj in orbits.keys():
    full[obj] = get_children(obj, orbits)

part1(full)
part2(full)

