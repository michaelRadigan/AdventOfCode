import collections
from aocd.models import Puzzle


def count_increases(pairs):
    return sum(next > current for current, next in pairs)


def solve_a(entries):
    return count_increases(zip(entries, entries[1:]))


def solve_b(entries):
    return count_increases(zip(entries, entries[3:]))


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=1)
    entries = [int(x) for x in puzzle.input_data.split()]

    solution_a = solve_a(entries)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(entries)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
