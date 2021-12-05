from typing import Counter
from aocd.models import Puzzle
import numpy as np

from recordclass import recordclass
from collections import defaultdict

# We're assuming that
Bingo = recordclass('Bingo', 'count grid_index')
MarkedGrid = recordclass('MarkedGrid', 'grid marked_sum')


def preprocess(grids):
    # I think that we want to preprocess the grids in a nice way

    # A lookup from a number to its relevent bingo
    bingo_lookup = defaultdict(list)

    # lookup from grid_index to grid, marked_count
    # Using a dict not an array for faster deletion
    marked_grid_lookup = {}

    for grid_index, grid in enumerate(grids):
        bingo_rows = {}
        bingo_columns = {}

        marked_grid_lookup[grid_index] = MarkedGrid(grid, 0)
        for i in range(grid.shape[0]):
            if i not in bingo_rows:
                bingo_rows[i] = Bingo(0, grid_index)
            for j in range(grid.shape[1]):
                if j not in bingo_columns:
                    bingo_columns[j] = Bingo(0, grid_index)

                num = grid[i][j]
                bingo_lookup[num].extend([bingo_rows[i], bingo_columns[j]])

    return bingo_lookup, marked_grid_lookup


def solve_a(bingo_lookup, marked_grid_lookup, numbers):
    for number in numbers:
        bingos = bingo_lookup[number]
        added = set()
        for bingo in bingos:
            bingo.count += 1
            marked_grid = marked_grid_lookup[bingo.grid_index]
            if bingo.grid_index not in added:
                added.add(bingo.grid_index)
                marked_grid.marked_sum += number

            if (bingo.count == 5):
                total = marked_grid.grid.sum() - marked_grid.marked_sum
                return total * number

    raise Exception("We never hit a bingo!")


# TODO[michaelr]: Should definitely clean up all of the duplication with part a here...
def solve_b(bingo_lookup, marked_grid_lookup, numbers):
    for number in numbers:
        bingos = bingo_lookup[number]
        added = set()
        for bingo in bingos:
            bingo.count += 1
            if bingo.grid_index in marked_grid_lookup:
                marked_grid = marked_grid_lookup[bingo.grid_index]
                if bingo.grid_index not in added:
                    added.add(bingo.grid_index)
                    marked_grid.marked_sum += number

                if (bingo.count == 5):
                    if bingo.grid_index in marked_grid_lookup:
                        del marked_grid_lookup[bingo.grid_index]

                    if len(marked_grid_lookup) == 0:
                        total = marked_grid.grid.sum() - marked_grid.marked_sum
                        return total * number

    raise Exception("We never hit a bingo!")


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=4)

    numbers_data, *grid_data = puzzle.input_data.strip().split("\n\n")
    numbers = map(int, numbers_data.split(","))
    grids = np.loadtxt(grid_data, dtype=int).reshape(-1, 5, 5)

    bingo_lookup_a, grid_lookup_a = preprocess(grids)
    bingo_lookup_b, grid_lookup_b = bingo_lookup_a.copy(), grid_lookup_a.copy()
    solution_a = solve_a(bingo_lookup_a, grid_lookup_a, numbers)

    solution_b = solve_b(bingo_lookup_b, grid_lookup_b, numbers)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
