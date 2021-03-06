import collections
from aocd.models import Puzzle


def solve_a(entries, target):
    seen = set()
    for entry in entries:
        partner = target - entry
        if partner in seen:
            return True, partner*entry
        seen.add(entry)
    return False, -1


def solve_b(entries):
    for i, entry in enumerate(entries):
        target = 2020 - entry
        possible, product = solve_a(entries[i+1:], target)
        if possible:
            return True, product*entry
    return False, -1


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=1)
    entries = [int(x) for x in puzzle.input_data.split()]
    solution_a = solve_a(entries, 2020)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    b_answer = solve_b(entries)
    print(f"Part B: {solution_a}")
    puzzle.answer_b = solution_a
