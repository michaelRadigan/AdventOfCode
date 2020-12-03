import collections
from aocd.models import Puzzle


def is_hash(iline):
    i, line = iline
    return line[i*3 % len(line)] == '#'


def solve_a(input_data):
    return sum(map(is_hash, enumerate(input_data.split('\n'))))


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=3)

    num_trees_a = solve_a(puzzle.input_data)
    print(f"Part A: {num_trees_a}")
    puzzle.answer_a = num_trees_a
