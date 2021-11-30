from aocd.models import Puzzle
from functools import reduce


# Bus has ID number
# Timestamp in minutes from fixed reference pont in the past

# I'm sure that there are countless libraries with CRM implemented, I just grabbed this from rosetta code
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod


def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1:
        return 1
    while a > 1:
        q = a // b
        a, b = b, a % b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0:
        x1 += b0
    return x1


def solve_a(earliest, buses):
    # We're going to have to cycle through the buses and just find the minimum I think

    min_time = 99999999999999999
    res = -1

    for bus in buses:
        revs = earliest // bus
        if revs % bus != 0:
            revs += 1
        time = revs*bus
        if time < min_time:
            min_time = time
            res = (time - earliest) * bus
    return res


def solve_b(buses):
    # ooo, this is pretty, we just need to find congruence (similar to finding d in RSA?)
    # I think we just implement extended euclidean and we're done
    # Ah, yep
    # https://en.wikipedia.org/wiki/Chinese_remainder_theorem#Search_by_sieving

    # So n is jut our buses
    a = [-bus[0] % bus[1] for bus in buses]
    n = [bus[1] for bus in buses]

    time = chinese_remainder(n, a)
    return time


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=13)
    lines = puzzle.input_data.splitlines()
    print(lines[1])
    earliest = int(lines[0])

    buses = list(map(int, filter(lambda num:
                                 str.isnumeric(num), lines[1].strip().split(","))))

    print(buses)

    answer_a = solve_a(earliest, buses)
    print(answer_a)
    puzzle.answer_a = answer_a

    # For part b we're going to need the numbered buses
    # In the interest of time, not going to reparse part a
    numbered_buses = [(i, int(bus)) for i, bus in enumerate(
        lines[1].strip().split(",")) if bus.isnumeric()]

    print(numbered_buses)

    answer_b = solve_b(numbered_buses)
    print(answer_b)
    puzzle.answer_b = answer_b
