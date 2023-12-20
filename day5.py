# day5.py

import pathlib
import sys

def getAlmanacMap(lines, index):
    almanacMap = []
    assert lines[index].endswith('map:')
    index += 1
    while index < len(lines) and lines[index]:
        almanacMap.append([int(i) for i in (lines[index]).split()])
        index += 1
    return almanacMap, index + 1

def parse(puzzle_input):
    lines = puzzle_input.split('\n')
    seeds = [int(i) for i in (lines[0].split('seeds: ')[1]).split()]

    seedToSoil, index = getAlmanacMap(lines, 2)
    soilToFertilizer, index = getAlmanacMap(lines, index)
    fertilizerToWater, index = getAlmanacMap(lines, index)
    waterToLight, index = getAlmanacMap(lines, index)
    lightToTemperature, index = getAlmanacMap(lines, index)
    temperatureToHumidity, index = getAlmanacMap(lines, index)
    humidityToLocation, index = getAlmanacMap(lines, index)

    return seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation

def calculateTransfer(sourceValue, mapSource):
    for destinationRangeStart, sourceRangeStart, rangeLength  in mapSource:
        if (sourceRangeStart <= sourceValue < sourceRangeStart + rangeLength):
            difference = sourceValue - sourceRangeStart
            return destinationRangeStart + difference
    return sourceValue

def seedToLocation(seed, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation):
    soil = calculateTransfer(seed, seedToSoil)
    fertilizer = calculateTransfer(soil, soilToFertilizer)
    water = calculateTransfer(fertilizer, fertilizerToWater)
    light = calculateTransfer(water, waterToLight)
    temperature = calculateTransfer(light, lightToTemperature)
    humidity = calculateTransfer(temperature, temperatureToHumidity)
    location = calculateTransfer(humidity, humidityToLocation)
    return location

def part1(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation):
    return min([seedToLocation(seed, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation) for seed in seeds])

def part2(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation):
    minLocation = sys.maxsize;
    # for i in range(0, len(seeds) -2, 2):
    #     startingSeed = seeds[i]
    #     seedRange = seeds[i+1]
    #     for s in range(startingSeed, startingSeed + seedRange):
    #         location = seedToLocation(s, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation)
    #         if location < minLocation:
    #             minLocation = location
    return minLocation

def solve(puzzle_input):
    """Solve the puzzle for the given input."""
    seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation = parse(puzzle_input)
    solution1 = part1(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation)
    solution2 = part2(seeds, seedToSoil, soilToFertilizer, fertilizerToWater, waterToLight, lightToTemperature, temperatureToHumidity, humidityToLocation)

    return solution1, solution2

if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(f"{path}:")
        puzzle_input = pathlib.Path(path).read_text().strip()
        solutions = solve(puzzle_input)
        print("\n".join(str(solution) for solution in solutions))
