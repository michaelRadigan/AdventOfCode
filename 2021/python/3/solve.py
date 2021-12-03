from typing import Counter
from aocd.models import Puzzle


def flip_bits(n, k):
    mask = (1 << k) - 1
    return n ^ mask


def solve_a(lines):
    binary_length = len(lines[0])

    theta = ''
    for i in range(binary_length):
        # Go through every binary number and grab the ith character
        vertical_strip = [binary[i] for binary in lines]
        strip_counter = Counter(vertical_strip)

        num_zeroes = strip_counter['0']
        num_ones = strip_counter['1']
        if num_zeroes > num_ones:
            theta += '0'
        else:
            theta += '1'

    theta_int = int(theta, 2)
    gamma_int = flip_bits(theta_int, binary_length)
    return theta_int * gamma_int


def solve_b(lines):
    # Ok, I don't think we're going to get a pretty solution today, let's just get a solution

    # Obviously there's loaaaads of duplication here (I'm hoping future me wil be bothered to clean it up)
    binary_length = len(lines[0])

    o2_lines = lines
    co2_lines = lines.copy()

    o2_rating = 0
    co2_rating = 0
    for i in range(binary_length):
        # Go through every binary number and grab the ith character
        o2_vertical_strip = [binary[i] for binary in o2_lines]
        co2_vertical_strip = [binary[i] for binary in co2_lines]
        o2_strip_counter = Counter(o2_vertical_strip)
        co2_strip_counter = Counter(co2_vertical_strip)

        if o2_strip_counter['0'] > o2_strip_counter['1']:
            # Keep '0'
            o2_lines = list(filter(
                lambda binary: binary[i] == '0', o2_lines))
        else:
            # Keep '1'
            o2_lines = list(filter(
                lambda binary: binary[i] == '1', o2_lines))

        if co2_strip_counter['1'] < co2_strip_counter['0']:
            # Keep '1'
            co2_lines = list(filter(
                lambda binary: binary[i] == '1', co2_lines))
        else:
            # Keep '0'
            co2_lines = list(filter(
                lambda binary: binary[i] == '0', co2_lines))

        if len(o2_lines) == 1:
            o2_rating = int(o2_lines[0], 2)
        if len(co2_lines) == 1:
            co2_rating = (int(co2_lines[0], 2))

        if o2_rating and co2_rating:
            return o2_rating * co2_rating

    return -1


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=3)
    lines = list(puzzle.input_data.split('\n'))

    # print(f"{lines=}")

    #solution_a = solve_a(lines)
    #print(f"Part A: {solution_a}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(lines)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
