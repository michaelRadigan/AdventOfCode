import collections
from aocd.models import Puzzle


def solve_a(pairs):
    depth = 0
    dist = 0
    for command, num in pairs:
        if command == 'down':
            depth += num
        elif command == 'up':
            depth -= num
        elif command == 'forward':
            dist += num
        else:
            raise Exception(f"oops {command=}, {num=}")

    return depth * dist


def solve_b(pairs):
    depth = 0
    dist = 0
    aim = 0
    for command, num in pairs:
        if command == 'down':
            aim += num
        elif command == 'up':
            aim -= num
        elif command == 'forward':
            dist += num
            depth += num * aim
        else:
            raise Exception(f"oops {command=}, {num=}")

    return depth * dist


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=2)
    entries = list(map(lambda pair: (pair[0], int(pair[1])), map(
        lambda x: x.split(), puzzle.input_data.split('\n'))))

    print(f"{entries=}")

    solution_a = solve_a(entries)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(entries)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
