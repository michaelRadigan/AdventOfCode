from aocd.models import Puzzle
from collections import defaultdict


def count_paths(edges, cave, seen):
    count = 0
    if cave == 'end':
        return 1
    if cave.islower():
        seen.add(cave)
    for next_cave in edges[cave]:
        if next_cave not in seen:
            count += count_paths(edges, next_cave, seen.copy())
    return count


def solve_a(edges):
    return count_paths(edges, 'start', set())


def count_paths_b(edges, cave, seen, ignore_used):
    count = 0
    if cave == 'end':
        return 1
    if cave.islower():
        seen.add(cave)
    for next_cave in edges[cave]:
        if next_cave in seen and next_cave.islower() and next_cave != "start" and not ignore_used:
            count += count_paths_b(edges, next_cave, seen.copy(), True)
        if next_cave not in seen:
            count += count_paths_b(edges, next_cave, seen.copy(), ignore_used)
    return count


def solve_b(edges):
    return count_paths_b(edges, 'start', set(), None)


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=12)
    edges = defaultdict(list)

    lines = puzzle.input_data.split('\n')

    for v1, v2 in map(lambda s: s.split('-'), lines):
        edges[v1].append(v2)
        edges[v2].append(v1)

    solution_a = solve_a(edges)
    print(f"{solution_a=}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(edges)
    print(f"{solution_b=}")
    puzzle.answer_b = solution_b
