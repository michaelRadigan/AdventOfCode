from aocd.models import Puzzle
from collections import Counter


def solve(fish_counter, days):
    for _ in range(days):
        new_day_counter = Counter()
        for (day, num_fish) in fish_counter.items():
            if day == 0:
                new_day_counter.update({6: num_fish, 8: num_fish})
            else:
                new_day_counter.update({day - 1: num_fish})
        fish_counter = new_day_counter
    return sum(fish_counter.values())


def solve_a(fish_counter):
    return solve(fish_counter, 80)


def solve_b(fish_counter):
    return solve(fish_counter, 256)


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=6)
    fish = Counter(int(num) for num in puzzle.input_data.split(','))

    solution_a = solve_a(fish)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve_b(fish)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
