from aocd.models import Puzzle
from functools import lru_cache


def solve_a(nums):
    single = 1
    triple = 1
    for i, j in zip(nums, nums[1:]):
        diff = j - i
        if diff == 1:
            single += 1
        elif diff == 3:
            triple += 1
        else:
            raise Exception("This should never ever happen")
    return single * triple


def find_perms(nums, i, seen):
    if i in seen:
        return seen[i]
    seen[i] = sum([find_perms(nums, j, seen)
                   for j in range(i+1, i+4) if j in nums])
    return seen[i]


def solve_b(nums):
    seen = {nums[-1]: 1}
    find_perms(nums, 0, seen)
    return seen[0]


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=10)
    nums = list(sorted(map(int, puzzle.input_data.split('\n'))))

    answer_a = solve_a(nums)
    print(answer_a)
    puzzle.answer_a = answer_a
    answer_b = solve_b(nums)
    print(answer_b)
    puzzle.answer_b = answer_b
