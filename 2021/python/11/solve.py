from aocd.models import Puzzle
from statistics import median
import numpy as np

adjecencies = [(-1, 1), (0, 1), (1, 1), (-1, 0),
               (1, 0), (-1, -1), (0, -1), (1, -1)]


# TODO: There's a lot of repitition here!
def solve_a(grid):
    flashes = 0
    for i in range(100):
        grid += 1
        to_flash = np.where(grid > 9)

        to_flash_list = [(i, j) for (i, j) in np.array(to_flash).T]
        flashed = set(to_flash_list)

        while to_flash_list:
            i, j = to_flash_list.pop(0)
            flashed.add((i, j))

            # This point is > 9 and can't be incremented any further
            for di, dj in adjecencies:
                adj_i, adj_j = i + di, j + dj
                if adj_i < 0 or adj_i > 9 or adj_j < 0 or adj_j > 9:
                    continue
                grid[adj_i][adj_j] = grid[adj_i][adj_j] + 1
                if grid[adj_i][adj_j] == 10:
                    to_flash_list.append(((adj_i, adj_j)))

        for (i, j) in flashed:
            flashes += 1
            grid[i][j] = 0

    return flashes


def solve_b(grid):
    # Let's have 400 as an upper bound
    for count in range(400):
        grid += 1
        to_flash = np.where(grid > 9)

        to_flash_list = [(i, j) for (i, j) in np.array(to_flash).T]
        flashed = set(to_flash_list)

        while to_flash_list:
            i, j = to_flash_list.pop(0)
            flashed.add((i, j))

            # This point is > 9 and can't be incremented any further
            for di, dj in adjecencies:
                adj_i, adj_j = i + di, j + dj
                if adj_i < 0 or adj_i > 9 or adj_j < 0 or adj_j > 9:
                    continue
                grid[adj_i][adj_j] = grid[adj_i][adj_j] + 1
                if grid[adj_i][adj_j] == 10:
                    to_flash_list.append(((adj_i, adj_j)))

        if (len(flashed) == 100):
            return count + 1

        for (i, j) in flashed:
            grid[i][j] = 0

    return -1


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=11)

    dummy_input = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

    grid = np.loadtxt([digit for line in puzzle.input_data.split('\n')
                      for digit in line], dtype=int).reshape(10, 10)

    # grid = np.loadtxt([digit for line in dummy_input.split('\n')
    #                   for digit in line], dtype=int).reshape(10, 10)

    #solution_a = solve_a(grid)
    # print(f"{solution_a=}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(grid)
    print(f"{solution_b=}")
    puzzle.answer_b = solution_b
