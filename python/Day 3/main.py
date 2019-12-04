from itertools import product

def man(x1, x2):
    return abs(x1) + abs(x2)

def solveA(wires):
    w1, w2 = wires
    pos = set()
    currX, currY = 0,0
    common = []
    for d, step in w1:
        if d == "U":
            for i in range(step+1):
                pos.add((currX, currY+i))
            currY += step
        if d == "R":
            for i in range(step+1):
                pos.add((currX+i, currY))
            currX += step
        if d == "D":
            for i in range(step+1):
                pos.add((currX, currY-i))
            currY -= step
        if d == "L":
            for i in range(step+1):
                pos.add((currX-i, currY))
            currX -= step
    pos.remove((0,0))
    currX, currY = 0,0
    for d, step in w2:
        if d == "U":
            for i in range(step+1):
                if (currX, currY+i) in pos:
                    common.append(man(currX, currY+i))
            currY += step
        if d == "R":
            for i in range(step+1):
                if (currX+i, currY) in pos:
                    common.append(man(currX+i, currY))
            currX += step
        if d == "D":
            for i in range(step+1):
                if (currX, currY-i) in pos:
                    common.append(man(currX, currY-i))
            currY -= step
        if d == "L":
            for i in range(step+1):
                if (currX-i, currY) in pos:
                    common.append(man(currX-i, currY))
            currX -= step
    print(common)
    return min(common, key=(lambda x : abs(x)))

def solveB(wires):
    w1, w2 = wires
    pos = {}
    currX, currY = 0,0
    common = []
    stepCount = 0
    for d, step in w1:
        if d == "U":
            for i in range(1,step+1):
                if (currX, currY+i) not in pos:
                    pos[(currX, currY+i)] = stepCount
                stepCount += 1
            currY += step
        if d == "R":
            for i in range(1,step+1):
                if (currX+i, currY) not in pos:
                    pos[(currX+i, currY)] = stepCount
                stepCount += 1
            currX += step
        if d == "D":
            for i in range(1,step+1):
                if (currX, currY-i) not in pos:
                    pos[(currX, currY-i)] = stepCount
                stepCount += 1
            currY -= step
        if d == "L":
            for i in range(1,step+1):
                if (currX-i, currY) not in pos:
                    pos[(currX-i, currY)] = stepCount
                stepCount += 1
            currX -= step
    # print(pos)
    # for k in sorted(pos): print k, pos[k]
    # pos.pop((0,0))
    currX, currY = 0,0
    stepCount = 0
    for d, step in w2:
        if d == "U":
            for i in range(1,step+1):
                if (currX, currY+i) in pos and (currX, currY+i) not in common:
                    common.append(pos[(currX, currY+i)]+stepCount)
                    print("Intersect in " + str(pos[(currX, currY+i)]) + " + " + str(stepCount) + " steps")
                stepCount += 1
            currY += step
        if d == "R":
            for i in range(1,step+1):
                if (currX+i, currY) in pos and (currX+i, currY) not in common:
                    common.append(pos[(currX+i, currY)]+stepCount)
                    print("Intersect in " + str(pos[(currX+i, currY)]) + " + " + str(stepCount) + " steps")
                stepCount += 1
            currX += step
        if d == "D":
            for i in range(1,step+1):
                if (currX, currY-i) in pos and (currX, currY-i) not in common:
                    common.append(pos[(currX, currY-i)]+stepCount)
                    print("Intersect in " + str(pos[(currX, currY-i)]) + " + " + str(stepCount) + " steps")
                stepCount += 1
            currY -= step
        if d == "L":
            for i in range(1,step+1):
                if (currX-i, currY) in pos and (currX-i, currY) not in common:
                    common.append(pos[(currX-i, currY)]+stepCount)
                    print("Intersect in " + str(pos[(currX-i, currY)]) + " + " + str(stepCount) + " steps")
                stepCount += 1
            currX -= step
    # print(common)
    return min(common)+2

def parser(inp):
    w1 = [(x[0], int(x[1:])) for x in inp[0].split(',')]
    w2 = [(x[0], int(x[1:])) for x in inp[1].split(',')]
    return w1, w2


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        inp = parser(inp.readlines())
        print(solveA(inp))
        print(solveB(inp))