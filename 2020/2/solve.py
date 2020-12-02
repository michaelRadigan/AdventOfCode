import collections
from aocd.models import Puzzle


def parse_line(line):
    nums, target, password = line.split(' ')
    i, j = nums.split('-')
    return int(i), int(j), target[0], password


def parse(input):
    return map(parse_line, input.split('\n'))


def is_valid_a(password_info):
    min_target, max_target, target, password = password_info
    return min_target <= password.count(target) <= max_target


def solve_a(password_infos):
    return len(list(filter(is_valid_a, password_infos)))


def is_valid_b(password_info):
    i, j, target, password = password_info

    def is_match(index, target, password):
        return password[index - 1] == target
    return is_match(i, target, password) != is_match(j, target, password)


def solve_b(password_infos):
    return len(list(filter(is_valid_b, password_infos)))


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=2)
    password_infos = list(parse(puzzle.input_data))
    solution_a = solve_a(password_infos)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(password_infos)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
