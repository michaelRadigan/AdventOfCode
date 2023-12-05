from aocd import get_data
from functools import reduce
from collections import defaultdict


def get_num_matches(line):
    # I could clean this up but I don't really want to right now (:
    return len(reduce(lambda x , y : x.intersection(y), [set(nums.split()) for nums in line.split(":")[1].strip().split("|")]))

def part_one(data):
    return sum(map(lambda x: 0 if len(x) == 0 else 2 ** (len(x) - 1), [reduce(lambda x , y : x.intersection(y), [set(nums.split()) for nums in line.split(":")[1].strip().split("|")]) for line in data.split("\n")]))


def part_two(data):
    cards = defaultdict(int)
    lines = data.split("\n")
    for i, line in enumerate(lines): 
        game_num = i + 1
        cards[game_num] += 1
        num_matches = get_num_matches(line)
        num_cards = cards[game_num]
        for i in range(1, num_matches + 1):
            cards[game_num + i] += num_cards
    return sum(cards.values())


if __name__ == "__main__":
    data = get_data(day=4, year=2023)
    print(f"{part_one(data)=}")
    print(f"{part_two(data)=}")
