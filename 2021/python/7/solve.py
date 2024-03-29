from aocd.models import Puzzle
from collections import Counter
from statistics import median, mean
from math import floor, ceil


def triangular(n):
    return n*(n+1) / 2


def solve_a(lines):
    med = median(lines)
    return int(sum(map(lambda h: abs(h - med), lines)))


def solve_b(lines):
    mean_point = mean(lines)

    def cost(square):
        return int(sum(map(lambda h: triangular(abs(h - square)), lines)))

    # The mean point can be between two squares, so check both and grab the min
    return min(cost(floor(mean_point)), cost(ceil(mean_point)))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=7)
    lines = [int(line) for line in puzzle.input_data.split(',')]

    solution_a = solve_a(lines)
    print(f"Part A: {solution_a}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(lines)
    print(f"Part B: {solution_b}")
    #puzzle.answer_b = solution_b
