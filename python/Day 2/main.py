from itertools import product

def executeProgram(memory):
    memory = memory.copy()
    pc = 0
    opcode = memory[pc]
    while opcode != 99:
        p1 = memory[pc+1]
        p2 = memory[pc+2]
        p3 = memory[pc+3]
        # print("Executing operation " + str(p1) + ": [" + str(p2) + "] + [" + str(p3) + "].")
        if opcode == 1:
            memory[p3] = memory[p1] + memory[p2]
        elif opcode == 2:
            memory[p3] = memory[p1] * memory[p2]
        else:
            raise Exception("Unknown opcode:" + str(opcode) + ".")
        pc += 4
        opcode = memory[pc]
    return memory

def solveA(memory):
    memory[1] = 12
    memory[2] = 2
    return executeProgram(memory)[0]

def solveB(memoryOrig):
    for noun, verb in product(range(100), range(100)):
        memory = memoryOrig.copy()
        memory[1] = noun
        memory[2] = verb
        try:
            if executeProgram(memory)[0] == 19690720:
                return 100 * noun + verb
        except:
            pass

def parser(inp):
    return [int(s) for s in inp[0].split(',')]


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        inp = parser(inp.readlines())
        print(solveA(inp))
        print(solveB(inp))