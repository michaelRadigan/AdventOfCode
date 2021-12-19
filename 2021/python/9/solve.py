from aocd.models import Puzzle
import heapq
from operator import mul
from functools import reduce

import numpy as np


def get_troughs(heights):
    padded_heights = np.pad(heights, mode='constant',
                            constant_values=9, pad_width=1)

    hor_indices = \
        (padded_heights[:, 1:-1] < padded_heights[:, 0:-2]) & \
        (padded_heights[:, 1:-1] < padded_heights[:, 2:])
    vert_indices = \
        (padded_heights[1:-1] < padded_heights[0:-2]) & \
        (padded_heights[1:-1] < padded_heights[2:])

    return hor_indices[1:-1] & vert_indices[:, 1:-1]


def solve_a(heights):
    # So, I have all of the heights, just need to filter for those thart are bigger than adjacent
    padded_heights = np.pad(heights, mode='constant',
                            constant_values=9, pad_width=1)

    hor_indices = \
        (padded_heights[:, 1:-1] < padded_heights[:, 0:-2]) & \
        (padded_heights[:, 1:-1] < padded_heights[:, 2:])
    vert_indices = \
        (padded_heights[1:-1] < padded_heights[0:-2]) & \
        (padded_heights[1:-1] < padded_heights[2:])

    troughs = heights[hor_indices[1:-1] & vert_indices[:, 1:-1]]
    risk_levels = troughs + 1
    return risk_levels.sum()


def solve_b(heights):
    padded_heights = np.pad(heights, mode='constant',
                            constant_values=9, pad_width=1)
    troughs = get_troughs(input)
    print(f"{troughs=}")
    trough_locations = np.where(troughs)

    # Adding one to get indices for the padded array
    lengths = []
    for (i, j) in np.array(trough_locations).T + 1:
        queue = []
        seen = set()
        queue.append((i, j))
        seen.add((i, j))
        basin_count = 0
        while queue:
            (x, y) = queue.pop()
            value = padded_heights[x][y]
            if value != 9:
                basin_count += 1
                for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                    transposed = (x + dx, y + dy)
                    if transposed not in seen:
                        seen.add(transposed)
                        queue.append(transposed)
        lengths.append(basin_count)

    largest = heapq.nlargest(3, lengths)
    return reduce(mul, largest)


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=9)

    input = np.array([num for line in puzzle.input_data.split('\n')
                      for num in line], dtype=int).reshape(100, 100)

    solution_a = solve_a(input)
    print(f"{solution_a=}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(input)
    print(f"{solution_b=}")
    puzzle.answer_b = solution_b
