# aoc202301.py

import pathlib
import sys
import re

def parse(puzzle_input):
    return puzzle_input.split('\n')

def findCalibrationValue(line):
    firstDigit = re.search("\d", line)
    lastDigit = re.search("\d(?!\S*\d)", line)
    return int(firstDigit.group() + lastDigit.group())

def replaceDigitStrings(line):
    str = line.replace('one', 'one1one')
    str = str.replace('two', 'two2two')
    str = str.replace('three', 'three3three')
    str = str.replace('four', 'four4four')
    str = str.replace('five', 'five5five')
    str = str.replace('six', 'six6six')
    str = str.replace('seven', 'seven7seven')
    str = str.replace('eight', 'eight8eight')
    str = str.replace('nine', 'nine9nine')
    return str

def part1(data):
    sum = 0
    for line in data:
        sum = sum + findCalibrationValue(line)
    return sum

def part2(data):
    sum = 0
    for line in data:
        str = replaceDigitStrings(line)
        sum = sum + findCalibrationValue(str)
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
