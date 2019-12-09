def part1():
    mini, minl = 100, layers[0]
    for l in layers:
        count = sum([x.count(0) for x in l])
        if mini > count:
            mini, minl = count, l
        
    count1 = sum([x.count(1) for x in minl])
    count2 = sum([x.count(2) for x in minl])
    print(count1*count2)


def part2():
    image = []
    for i in range(height):
        image.append([])
        for j in range(width):
            layer = 0
            while layers[layer][i][j] == 2:
                layer += 1

            image[i].append('.' if layers[layer][i][j] else ' ')

    # Pretty print this
    [print(''.join(x)) for x in image]


with open("input.txt") as f:
    lst = list(map(int, f.read()))

layers = []
width = 25
height = 6

while len(lst):
    layer = []
    for i in range(height):
        layer.append([])

        for j in range(width):
            layer[i].append(lst.pop(0))

    layers.append(layer)

part1()
part2()
