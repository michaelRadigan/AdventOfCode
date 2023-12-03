from typing import List
from collections import defaultdict
from math import prod

from aocd import get_data
from icecream import ic

def part_one(arr: List[List[str]]):
    num_rows = len(arr)
    num_cols = len(arr[0])

    def search_is_part(row, col):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x = col + dx
                y = row + dy
                if 0 <= x < num_cols and 0 <= y < num_rows:
                    adjacent_val = arr[y][x]
                    if not (adjacent_val.isdigit() or adjacent_val == '.'):
                        return True
        return False   
    
    count = 0
    for row, row_arr in enumerate(arr):
        current_num = 0
        is_part = False
        for col, val in enumerate(row_arr):
            if val.isdigit():
                current_num = current_num * 10 + int(val)
                is_part = is_part or search_is_part(row, col)
            else:
                # We will have already seached this spot and so we just need to add it to our 
                if is_part:
                    count += current_num
                current_num = 0    
                is_part = False
        if is_part:
            count += current_num
    return count

def part_two(arr: List[List[str]]):
    gears = defaultdict(set)
    all_parts = {}

    num_rows = len(arr)
    num_cols = len(arr[0])

    def search_for_gears(row, col, part_num):
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                if dx == 0 and dy == 0:
                    continue
                x = col + dx
                y = row + dy
                if 0 <= x < num_cols and 0 <= y < num_rows:
                    adjacent_val = arr[y][x]
                    if adjacent_val == '*':
                        parts_in_gear = gears[(y, x)]
                        parts_in_gear.add(part_num)
                        gears[(y, x)] = parts_in_gear
    
    count = 0
    part_num = 0
    for row, row_arr in enumerate(arr):
        current_num = 0
        for col, val in enumerate(row_arr):
            if val.isdigit():
                current_num = current_num * 10 + int(val)
                search_for_gears(row, col, part_num)
            else:
                if current_num != 0:
                    all_parts[part_num] = current_num
                current_num = 0
                part_num += 1
        # We may have reached the end of the row within a number but we should still register this as a part
        if current_num != 0:
            all_parts[part_num] = current_num

    for part_num_set in gears.values():
        if len(part_num_set) == 2:
            ratio = prod([all_parts[part_num] for part_num in part_num_set])
            count += ratio
    return count

if __name__ == "__main__":
    data = get_data(day=3, year=2023)
    arr = [list(line) for line in data.split('\n')]
    ic(part_one(arr))
    ic(part_two(arr))

