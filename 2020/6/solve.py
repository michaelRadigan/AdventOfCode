import collections
from aocd.models import Puzzle
import functools

if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=6)
    # Don't think that today is going to be pretty, let's just smash a one liner instead
    total_count_a = sum(map(
        lambda group: len(set(group.replace('\n', ''))), puzzle.input_data.split('\n\n')))

    print(f"{total_count=}")
    puzzle.answer_a = total_count
    # print(f"{my_allocation=}")
    # puzzle.answer_b=my_allocation
