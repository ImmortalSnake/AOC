from itertools import permutations

def run(intops, inputs, ip=0, inn=0):
    num_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3]

    while intops[ip] % 100 != 99:
        modes = [intops[ip] // (10 ** x) % 10 for x in range(2, 5)]
        op = intops[ip] % 100

        operands = [intops[ip + x + 1] if modes[x] == 1 else intops[intops[ip + x + 1]]
                    for x in range(num_operands[op])]

        if op == 1 or op == 2:
            intops[intops[ip + 3]] = operands[0] + operands[1] if op == 1 else operands[0] * operands[1]

        elif op == 3:
            intops[intops[ip + 1]] = inputs[inn]
            inn += 1

        elif op == 4:
            return operands[0], False, ip
            
        elif op == 5 or op == 6:
            if (op == 5 and operands[0] != 0) or (op == 6 or operands[0] == 0):
                ip = operands[1] - 3

        elif op == 7 or op == 8:
            if (op == 7 and operands[0] < operands[1]) or (op == 8 and operands[0] == operands[1]):
                intops[intops[ip + 3]] = 1
            else:
                intops[intops[ip + 3]] = 0
        else:
            print("ERROR!")
            break

        ip += num_operands[op] + 1
        
    return 0, True, ip


def part1():
    perm = list(permutations(range(5)))
    outputs = []
    for inputs in perm:
        o1 = run(lst[:], (inputs[0], 0))
        o2 = run(lst[:], (inputs[1], o1[0]))
        o3 = run(lst[:], (inputs[2], o2[0]))
        o4 = run(lst[:], (inputs[3], o3[0]))
        o5 = run(lst[:], (inputs[4], o4[0]))
        
        outputs.append(o5[0])

    print(max(outputs))


def part2():
    perms = list(permutations(range(5, 10)))
    outputs = []
    for perm in perms:
        intcodes = [lst[:] for _ in range(5)]
        pointers = [0, 0, 0, 0, 0]
        input_signals = [0]
        i = 0
        inn = 0
        
        while True:
            output = run(intcodes[i], (perm[i], input_signals[-1]), pointers[i], inn)
            pointers[i] = output[2]
            input_signals.append(output[0])
            i = (i+1) % 5

            if i == 0:
                inn = 1
            if output[1]:
                break

        outputs.append(input_signals[-2])

    print(max(outputs))


with open("input.txt") as f:
    lst = list(map(int, f.read().split(',')))

part1()
part2()
