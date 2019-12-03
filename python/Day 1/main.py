def getFuel(mass):
    return int(mass / 3) - 2

def getTotalFuel(mass):
    fuel = 0
    while getFuel(mass) > 0:
        mass = getFuel(mass)
        fuel += mass
    return fuel

def solveA(modulesMasses):
    fuel = 0
    for line in inp:
        fuel += getFuel(int(line))
    return fuel

def solveB(modulesMasses):
    fuel = 0
    for line in inp:
        fuel += getTotalFuel(int(line))
    return fuel


if __name__ == "__main__":
    with open("input.txt", "r") as inp:
        inp = inp.readlines()
        print(solveA(inp))
        print(solveB(inp))