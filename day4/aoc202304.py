# aoc202304.py

import pathlib
import sys
import numpy as np
from rich import print
from rich import pretty
pretty.install()

def parse(puzzle_input):
    rows = puzzle_input.split('\n')
    data = []
    for line in rows:
        winningNumbers = line[line.find(':')+1:line.find("|")]
        winningNumbers = winningNumbers.strip()
        myNumbers = line[line.find('|')+1:]
        myNumbers = myNumbers.strip()
        data.append((winningNumbers, myNumbers))
    return data

def countMatches(card):
    count = 0
    myNums = card[1].split()
    winningNums = card[0].split()
    for myNum in myNums:
        if myNum in winningNums:
            count += 1
    return count

def part1(data):
    sum = 0
    for card in data:
        count = countMatches(card)
        if count != 0:
            sum += 2**(count - 1)
    return sum

def part2(data):
    cardInstances = np.ones(len(data), dtype=int)
    
    for index, card in enumerate(data):
        count = countMatches(card)
        for i in range(count):
            cardInstances[index+i+1] += cardInstances[index]

    total_scratchcards = sum(cardInstances)
    return total_scratchcards

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
