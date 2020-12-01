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


if __name__ == "__main__":
    with open("2020/1/input.txt", "r") as f:
        entries = [int(x) for x in f.read().split()]
    print(f"Part A: {solve_a(entries)}")
