from aocd.models import Puzzle
from collections import Counter
from statistics import median


def triangular(n):
    return n*(n+1) / 2


def solve_a(lines):
    med = median(lines)
    return int(sum(map(lambda h: abs(h - med), lines)))


def solve_b(lines):
    minimum = min(lines)
    maximum = max(lines)
    min_fuel = 999999999
    for i in range(minimum, maximum+1):
        fuel = int(sum(map(lambda h: triangular(abs(h - i)), lines)))
        min_fuel = min(min_fuel, fuel)
    return min_fuel


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=7)
    lines = [int(line) for line in puzzle.input_data.split(',')]

    solution_a = solve_a(lines)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(lines)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
