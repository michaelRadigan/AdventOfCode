import collections
from aocd.models import Puzzle


def solve_a(entries):
    return sum([next > current for current, next in zip(entries, entries[1:])])


def solve_b(entries):
    summed_windows = [sum(window)
                      for window in zip(entries, entries[1:], entries[2:])]
    return solve_a(summed_windows)


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=1)
    entries = [int(x) for x in puzzle.input_data.split()]

    solution_a = solve_a(entries)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(entries)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
