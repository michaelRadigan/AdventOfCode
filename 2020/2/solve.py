import collections
from aocd.models import Puzzle


def parse(input):

    def parse_line(line):
        nums, target, password = line.split(' ')
        i, j = nums.split('-')
        return int(i), int(j), target[0], password

    return map(parse_line, input.split('\n'))


def solve(password_infos, is_valid):
    return sum(map(is_valid, password_infos))


def is_valid_a(password_info):
    min_target, max_target, target, password = password_info
    return min_target <= password.count(target) <= max_target


def is_valid_b(password_info):
    i, j, target, password = password_info

    def is_match(index, target, password):
        return password[index - 1] == target
    return is_match(i, target, password) != is_match(j, target, password)


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=2)
    password_infos = list(parse(puzzle.input_data))
    solution_a = solve(password_infos, is_valid_a)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve(password_infos, is_valid_b)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
