import collections
from aocd.models import Puzzle
import itertools


def is_hash(i, line, dx, dy):
    return line[i*dx % len(line)] == '#'


def solve_a(input_data):
    return sum(map(lambda iline: is_hash(iline[0], iline[1], 3, 1), enumerate(input_data.split('\n'))))


def solve_b(input_data):
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    product = 1
    for dx, dy in slopes:
        num_trees_for_slope = sum(map(lambda iline: is_hash(
            iline[0], iline[1], dx, dy), enumerate(input_data.split('\n')[::dy])))
        product *= num_trees_for_slope
    return product


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=3)

    num_trees_a = solve_a(puzzle.input_data)
    print(f"Part A: {num_trees_a}")
    puzzle.answer_a = num_trees_a

    product_trees_b = solve_b(puzzle.input_data)
    print(f"Part B: {product_trees_b}")
    puzzle.answer_b = product_trees_b
