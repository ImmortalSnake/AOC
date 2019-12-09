def run(intops):
    num_operands = [0, 3, 3, 1, 1, 2, 2, 3, 3, 1, 1]
    rb = ip = 0
    
    while intops[ip] % 100 != 99:
        modes = [intops[ip] // (10 ** x) % 10 for x in range(2, 5)]
        op = intops[ip] % 100
        
        operands = [intops[ip+x+1] if modes[x] == 1 else intops[(rb if modes[x] == 2 else 0) + intops[ip+x+1]]
                    for x in range(num_operands[op])]
        
        if op == 1:
            intops[(rb if modes[2] == 2 else 0) + intops[ip+3]] = operands[0] + operands[1]

        elif op == 2:
            intops[(rb if modes[2] == 2 else 0) + intops[ip+3]] = operands[0] * operands[1]

        elif op == 3:
            intops[(rb if modes[0] == 2 else 0) + intops[ip+1]] = int(input("Enter input: "))
            
        elif op == 4:
            print(operands[0])
            
        elif op == 5 or op == 6:
            if (op == 5 and operands[0] != 0) or (op == 6 and operands[0] == 0):
                ip = operands[1] - 3

        elif op == 7 or op == 8:
            if (op == 7 and operands[0] < operands[1]) or (op == 8 and operands[0] == operands[1]):
                intops[(rb if modes[2] == 2 else 0) + intops[ip+3]] = 1
            else:
                intops[(rb if modes[2] == 2 else 0) + intops[ip+3]] = 0

        elif op == 9:
            rb += operands[0]
        else:
            print("ERROR!")
            break

        ip += num_operands[op] + 1
        
    return intops


with open("input.txt") as f:
    run(list(map(int, f.read().split(',')))+[0]*1000)

