from aocd.models import Puzzle
from collections import Counter


def solve_a(coords):

    counter = Counter()
    for ((x0, y0), (x1, y1)) in coords:
        if x0 == x1:
            min_y = min(y0, y1)
            max_y = max(y0, y1)
            counter.update([(x0, j) for j in range(min_y, max_y + 1)])
        elif y0 == y1:
            min_x = min(x0, x1)
            max_x = max(x0, x1)
            counter.update([(i, y0) for i in range(min_x, max_x + 1)])

    num = len([count for count in counter.values() if count >= 2])
    return num


def solve_b(coords):
    counter = Counter()
    for ((x0, y0), (x1, y1)) in coords:
        if x0 == x1:
            min_y = min(y0, y1)
            max_y = max(y0, y1)
            counter.update([(x0, j) for j in range(min_y, max_y + 1)])
        elif y0 == y1:
            min_x = min(x0, x1)
            max_x = max(x0, x1)
            counter.update([(i, y0) for i in range(min_x, max_x + 1)])
        else:
            if x0 < x1:
                diff = x1 - x0
                if y0 < y1:
                    counter.update([(x0 + i, y0 + i)
                                    for i in range(diff + 1)])
                else:
                    counter.update([(x0 + i, y0 - i)
                                    for i in range(diff + 1)])
            else:
                diff = x0 - x1
                if y0 < y1:
                    counter.update([(x0 - i, y0 + i)
                                    for i in range(diff + 1)])
                else:
                    counter.update([(x0 - i, y0 - i)
                                    for i in range(diff + 1)])

    num = len([count for count in counter.values() if count >= 2])
    return num


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=5)

    def parse(line):
        pairs = line.split("->")
        [(x0, y0), (x1, y1)] = [map(int, p.strip().split(',')) for p in pairs]
        return ((x0, y0), (x1, y1))

    coords = [parse(line) for line in puzzle.input_data.split('\n')]

    solution_a = solve_a(coords)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(coords)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
