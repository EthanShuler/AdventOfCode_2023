# aoc202302.py

import pathlib
import sys
import re

maxRed = 12
maxGreen = 13
maxBlue = 14

def parse(puzzle_input):
    return puzzle_input.split('\n')

def pairHasmoreCubesThanMax(round):
    str = round.strip()
    pair = str.split(' ')
    if (pair[1] == 'red'):
        if int(pair[0]) > maxRed:
            return True
    elif (pair[1] == 'green'):
        if int(pair[0]) > maxGreen:
            return True
    elif (pair[1] == 'blue'):
        if int(pair[0]) > maxBlue:
            return True
    return False

def anyColorCountsOver(line):
    games = line.split(':')[1]
    rounds = re.split(',|;', games)
    for round in rounds:
        if pairHasmoreCubesThanMax(round):
            return True
    return False

def part1(data):
    sum = 0
    for i, line in enumerate(data):
        id = i+1
        if (not anyColorCountsOver(line)):
            sum = sum + id
    return sum

def getColorMapForRow(games):
    gamesSplit = re.split(',|;', games)
    colorMap = {
        "red": -1,
        "green": -1,
        "blue": -1
    }
    for game in gamesSplit:
        str = game.strip()
        pair = str.split(' ')
        color = pair[1]
        num = int(pair[0])
        if num > colorMap[color]:
            colorMap[color] = num
    return colorMap

def part2(data):
    sum = 0
    for line in data:
        games = line.split(':')[1]
        colorMap = getColorMapForRow(games)
        power = colorMap['red'] * colorMap['green'] * colorMap['blue']
        sum = sum + power
    return sum

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
