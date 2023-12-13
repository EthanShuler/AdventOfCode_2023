# aoc202303.py

import pathlib
import sys
import re
from rich import print
from rich import pretty
pretty.install()

def parse(puzzle_input):
    rows = puzzle_input.split('\n')
    return rows

def part1(data):
    sum = 0
   
    return sum
            

def part2(data):
    return 0;

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
