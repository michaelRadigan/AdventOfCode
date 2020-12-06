import collections
from aocd.models import Puzzle
import functools


def sum_arithmetic_series(N):
    return N * (N + 1) // 2


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=5)

    mappings = str.maketrans({'B': '1', 'F': '0', 'R': '1', 'L': '0'})
    cipher_allocations = puzzle.input_data.split()

    # Apologies for the plaintext/plane pun, I couldn't resist
    # Note that row*8+5 is done for us implicitly
    plain_allocations = list(map(lambda line: int(
        line.translate(mappings), 2), cipher_allocations))

    min_allocation = min(plain_allocations)
    max_allocation = max(plain_allocations)
    sum_allocations = sum(plain_allocations)

    sum_to_max = sum_arithmetic_series(max_allocation)
    sum_to_min = sum_arithmetic_series(min_allocation-1)
    expected_sum_allocations = sum_to_max - sum_to_min
    my_allocation = expected_sum_allocations - sum_allocations

    print(f"{max_allocation=}")
    puzzle.answer_a = max_allocation
    print(f"{my_allocation=}")
    puzzle.answer_b = my_allocation
