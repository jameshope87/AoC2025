import os
import pathlib
from operator import add, sub

DAY = 1

FILEPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}input.txt')
TESTPATH = os.path.join(pathlib.Path(__file__).parent.absolute(), f'day{DAY}test.txt')

def fileHandling(filepath: str) -> list[str]:
    with open(filepath, 'r') as file:
        data = file.read().splitlines()
    return data

def parseInput(command: str) -> tuple[str, int]:
    operators = {'R': sub, 'L': add}
    direction = operators[command[0]]
    magnitude = int(command[1:])
    return direction, magnitude

def main(test:bool = False, part2:bool = False):
    filepath = TESTPATH if test else FILEPATH
    data = fileHandling(filepath)
    #print(f"Data Loaded: {data}")
    pos = 50
    zeroCounter = 0
    if not part2:
        for command in data:
            direction, magnitude = parseInput(command)
            pos = direction(pos, magnitude) % 100
            if pos == 0:
                zeroCounter += 1
        return zeroCounter
    else:
        for command in data:
            direction, magnitude = parseInput(command)
            fullRotations, steps = divmod(magnitude, 100)
            newPos = direction(pos, steps)
            passed_or_landed = int(pos != 0 and not(0 < newPos <100))
            zeroCounter += fullRotations + passed_or_landed
            pos = newPos % 100
        return zeroCounter



if __name__ == "__main__":
    print("Running Test Data for Part 1")
    result = main(test=True, part2=False)
    print(f"Result: {result}")
    print("Running Actual Data for Part 1")
    result = main(test=False, part2=False)
    print(f"Result: {result}")
    print("Running Test Data for Part 2")
    result = main(test=True, part2=True)
    print(f"Result: {result}")
    print("Running Actual Data for Part 2")
    result = main(test=False, part2=True)
    print(f"Result: {result}")