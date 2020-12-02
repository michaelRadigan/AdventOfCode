import collections
from aocd.models import Puzzle


def parse_line(line):
    nums, target, password = line.split(' ')
    min_target, max_target = nums.split('-')
    return int(min_target), int(max_target), target[0], password


def is_valid(parsed_line):
    min_target, max_target, target, password = parsed_line
    return min_target <= password.count(target) <= max_target


def solve_a(input):
    count = 0
    parsed_lines = map(parse_line, input.split('\n'))
    for _ in filter(is_valid, parsed_lines):
        count += 1
    return count


def solve_b():
    pass


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=2)
    solution_a = solve_a(puzzle.input_data)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    #b_answer = solve_b(entries)
    #print(f"Part B: {solve_b(entries)}")
    #puzzle.answer_b = b_answer
