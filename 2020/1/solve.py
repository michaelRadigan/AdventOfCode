import os
import collections


def solve_a(entries, target):
    seen = set()
    for entry in entries:
        partner = target - entry
        if partner in seen:
            return True, partner*entry
        seen.add(entry)
    return False, -1


def solve_b(entries):
    for i, entry in enumerate(entries):
        target = 2020 - entry
        possible, product = solve_a(entries[i+1:], target)
        if possible:
            return True, product*entry
    return False, -1


if __name__ == "__main__":
    with open("2020/1/input.txt", "r") as f:
        entries = [int(x) for x in f.read().split()]
    print(f"Part A: {solve_a(entries, 2020)}")
    print(f"Part B: {solve_b(entries)}")
