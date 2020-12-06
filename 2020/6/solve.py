import collections
from aocd.models import Puzzle
import functools

if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=6)
    # Don't think that today is going to be pretty, let's just smash a one liner instead
    total_count_a = sum(map(
        lambda group: len(set(group.replace('\n', ''))), puzzle.input_data.split('\n\n')))

    # Part b also seems a bit lame, filthy one liner here as well with whatever formatting PEP8 decides, I'm sorry
    total_count_b = sum(map(lambda answers: len(functools.reduce(set.intersection, answers)), map(
        lambda group: map(set, group.split('\n')), puzzle.input_data.split('\n\n'))))

    print(f"{total_count_a=}")
    puzzle.answer_a = total_count_a
    print(f"{total_count_b=}")
    puzzle.answer_b = total_count_b
