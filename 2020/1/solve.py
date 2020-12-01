import os
import collections


def solve_a(entries):
    seen = set()
    for entry in entries:
        partner = 2020 - entry
        if partner in seen:
            return partner*entry
        seen.add(entry)
    return -1


def solve_b(entries):
    for i, entry in enumerate(entries):
        seen = set()
        target = 2020 - entry
        for partner in entries[i+1:]:
            if (target - partner) in seen:
                return entry*partner*(target-partner)
            seen.add(partner)
    return -1


if __name__ == "__main__":
    with open("2020/1/input.txt", "r") as f:
        entries = [int(x) for x in f.read().split()]
    print(f"Part A: {solve_a(entries)}")
    print(f"Part B: {solve_b(entries)}")
