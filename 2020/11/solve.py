from aocd.models import Puzzle
from copy import deepcopy

# . - floor
# L - empty
# # - occupied

# Leaving this in as a reminder to future me that I spent a long time debugging this becuase I got the adjacencies wrong...
# adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
#             (0, 1), (1, -1), (0, -1), (1, -1)]

adjacents = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
             (0, 1), (1, -1), (1, 0), (1, 1)]


def num_occupied_direct_neighbours(grid, i, j):
    # This can probably just be a list comprehension
    acc = 0
    for di, dj in adjacents:
        adjacent_i, adjacent_j = i+di, j+dj
        if 0 <= adjacent_i < num_rows and 0 <= adjacent_j < num_cols and grid[adjacent_i][adjacent_j] == '#':
            acc += 1
    return acc


def num_occupied(grid, i, j):
    acc = 0
    for di, dj in adjacents:
        adjacent_i, adjacent_j = i+di, j+dj
        while 0 <= adjacent_i < num_rows and 0 <= adjacent_j < num_cols:
            cell = grid[adjacent_i][adjacent_j]
            if cell == 'L':
                break
            elif cell == '#':
                acc += 1
                break
            adjacent_i += di
            adjacent_j += dj

    return acc


def next(grid, count_neighbours, threshhold):
    new_grid = deepcopy(grid)
    num_changes = 0
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            num_neighbours = count_neighbours(grid, i, j)
            if cell == 'L' and num_neighbours == 0:
                new_grid[i][j] = '#'
                num_changes += 1
            elif cell == '#' and num_neighbours >= threshhold:
                new_grid[i][j] = 'L'
                num_changes += 1
    return num_changes, new_grid


def solve_a(grid):
    num_changes, new_grid = next(grid, num_occupied_direct_neighbours, 4)

    count = 0
    while(num_changes > 0):
        # This is really inefficient but at this point I'm not that fussed
        # Also a bit sad that there isn't reuse between this and counting the occupied neighbours :(
        num_changes, new_grid = next(
            new_grid, num_occupied_direct_neighbours, 4)
    total_occupied = sum(row.count('#') for row in new_grid)
    return total_occupied


def solve_b(grid):
    # We should really remove some redundancy between a and b after we catch up :)

    num_changes, new_grid = next(grid, num_occupied, 5)

    count = 0
    while(num_changes > 0):
        # This is really inefficient but at this point I'm not that fussed
        # Also a bit sad that there isn't reuse between this and counting the occupied neighbours :(
        num_changes, new_grid = next(new_grid, num_occupied, 5)
    total_occupied = sum(row.count('#') for row in new_grid)
    return total_occupied


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=11)
    grid = list(map(list, map(str.rstrip, puzzle.input_data.splitlines())))
    num_cols = len(grid[0])
    num_rows = len(grid)

    answer_a = solve_a(grid)
    print(f"{answer_a=})
    #puzzle.answer_a = answer_a
    answer_b = solve_b(grid)
    print(f"{answer_b=}")
    puzzle.answer_b = answer_b
