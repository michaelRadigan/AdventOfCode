from aocd import get_data
from functools import reduce

def part_one(data):
    return sum(map(lambda x: 0 if len(x) == 0 else 2 ** (len(x) - 1), [reduce(lambda x , y : x.intersection(y), [set(nums.split()) for nums in line.split(":")[1].strip().split("|")]) for line in data.split("\n")]))
    
def part_two(data):
    pass

if __name__ == "__main__":
    data = get_data(day=4, year=2023)
    print(f"{part_one(data)=}")
