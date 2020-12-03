import collections
from aocd.models import Puzzle
import itertools


def is_hash(i, line, dx, dy):
    return line[i*dx % len(line)] == '#'


def solve(input_data, slopes):
    product = 1
    for dx, dy in slopes:
        ilines = enumerate(input_data.split('\n')[::dy])
        product *= sum(map(
            lambda iline: is_hash(iline[0], iline[1], dx, dy), ilines))
    return product


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=3)

    num_trees_a = solve(puzzle.input_data, [(3, 1)])
    print(f"Part A: {num_trees_a}")
    puzzle.answer_a = num_trees_a

    slopes_b = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product_trees_b = solve(puzzle.input_data, slopes_b)
    print(f"Part B: {product_trees_b}")
    puzzle.answer_b = product_trees_b
