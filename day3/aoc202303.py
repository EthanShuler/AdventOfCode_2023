# aoc202303.py

import pathlib
import sys
import re
from rich import print
from rich import pretty
pretty.install()

def parse(puzzle_input):
    rows = puzzle_input.split('\n')
    rows.append('.'*len(rows[0]))
    rows.insert(0, '.'*len(rows[0]))
    output = []
    for line in rows:
        line = '.' + line + '.'
        output.append(line)
    return output

def part1(data):
    sum = 0
    for rowNum, line in enumerate(data):       
        for match in re.finditer(r'\d+', line):
            s = match.start()
            e = match.end()
            # look above
            if re.search(r'[^\d\.]', data[rowNum - 1][s-1:e+1]):
                sum += int(line[s:e])
                continue
            # look below
            if re.search(r'[^\d\.]', data[rowNum + 1][s-1:e+1]):
                sum += int(line[s:e])
                continue
            # look left
            if re.search(r'[^\d\.]', line[s-1:s]):
                sum += int(line[s:e])
                continue
            # look right
            if re.search(r'[^\d\.]', line[e:e+1]):
                sum += int(line[s:e])
                continue
    return sum

def part2(data):
    sum = 0
    gears = {}
    for positionX, line in enumerate(data):
        for positionY, char in enumerate(line):
            if char == '*':
                gears[(positionX, positionY)] = []
    for positionX, line in enumerate(data):
        for match in re.finditer(r'\d+', line):
            s = match.start()
            e = match.end()
            # look above
            gearPos = data[positionX - 1].find('*', s-1, e+1) 
            if (gearPos != -1 and ((positionX-1, gearPos) in gears)):
                gears[(positionX-1, gearPos)].append(line[s:e])
            # look below
            gearPos = data[positionX + 1].find('*', s-1, e+1) 
            if (gearPos != -1 and ((positionX+1, gearPos) in gears)):
                gears[(positionX+1, gearPos)].append(line[s:e])
            # look left
            gearPos = line.find('*', s-1, s) 
            if (gearPos != -1 and ((positionX, gearPos) in gears)):
                gears[(positionX, gearPos)].append(line[s:e])
            # look right
            gearPos = line.find('*', e, e+1) 
            if (gearPos != -1 and ((positionX, gearPos) in gears)):
                gears[(positionX, gearPos)].append(line[s:e])
    for gearValues in gears.values():
        if len(gearValues) == 2:
            sum += (int(gearValues[0]) * int(gearValues[1]))
    return sum;

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    data = parse(puzzle_input)
    solution1 = part1(data)
    solution2 = part2(data)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
