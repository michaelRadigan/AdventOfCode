from aocd import get_data
from dataclasses import dataclass
from typing import List, Tuple

@dataclass
class SingleMapping:
    """
    A simple mapping used for part 1 
    """
    source_start: int # start_inclusive
    source_end: int # end_inclusive
    dest_start: int # start_inclusive
    dest_end: int # end_inclusive

def solve(seeds, sections):
    def construct_mapping(section):
        def make_single_mapping(line):
            dest_start, source, map_range = map(int, line.split(" "))
            return SingleMapping(source_start=source, source_end=source+map_range-1, dest_start=dest_start, dest_end=dest_start+map_range-1)
        mapping = [make_single_mapping(line) for line in section.split("\n")[1:]]
        # WE should sort here

        # Initially, we're just going to sort by start value
        mapping.sort(key=lambda m: m.source_start)
        return mapping
    
    mappings = [construct_mapping(section) for section in sections[1:]]

    def map_val(current_val, mapping):
        for single_mapping in mapping:
            if current_val < single_mapping.source_start: 
                return current_val
            elif single_mapping.source_start <= current_val <= single_mapping.source_end:
                dist = current_val - single_mapping.source_start
                return single_mapping.dest_start + dist
        return current_val
    min_mapping = 1e16
    print(len(seeds))
    for i, seed in enumerate(seeds):
        if i % 1000 == 0:
            print(i)
        current_val = seed
        for mapping in mappings:
            current_val = map_val(current_val, mapping)
                # We could binary chop, instead I'm going to just linear scan, I think we have few enough inputs that this is ok, for now
        min_mapping = min(current_val, min_mapping)

    return min_mapping 
    
def part_one(data):
    # seeds_str, seed_to_soil_str, soil_to_fert_str, fert_to_water_str, water_to_light_str, light_to_temp_str, temp_to_hum_str, hum_to_loc_str = data.split("\n\n")
    sections = data.split("\n\n")
    seeds = list(map(int, sections[0].split(":")[1].split()))        
    return solve(seeds, sections)

@dataclass
class Function:
    """
    Going to redo things to get a clean solution to part two :) 
    """
    source_start: int
    source_end: int # just more convention, note that this is a _non-inclusive_ bound
    dest_start: int
    range_len: int       
    
class Mapping():
    def _make_function(self, line):
        dest_start, source_start, range_len = map(int, line.split(" "))
        return Function(source_start, source_start + range_len, dest_start, range_len)

    def __init__(self, mapping_def) -> None:
        self.functions =  [self._make_function(line) for line in mapping_def.split("\n")[1:]]
        # So, I think that all of the functions are actually non-overlapping sop we don't need to sort by start/end here
        # self.functions.sort(by=)
            
    def map_ranges(self, ranges: List[Tuple[int, int]]):
        mapped = []
        to_map = ranges
        for function in self.functions:
            still_not_mapped = []
            while to_map:
                range_start, range_end = to_map.pop(0)
                # We have three categories for each function: pre, inner and outer:
                # [pre... .....inner..........outer     )
                #        [                   )
                start_pre = range_start
                end_pre = min(range_end, function.source_start)
                if start_pre < end_pre:
                    still_not_mapped.append((start_pre, end_pre))

                start_inner = max(range_start, function.source_start)
                end_inner = min(range_end, function.source_end)
                if start_inner < end_inner:
                    diff = function.dest_start - function.source_start
                    mapped.append((start_inner + diff, end_inner + diff))

                start_outer = max(range_start, function.source_end)
                end_outer = range_end
                if start_outer < end_outer:
                    still_not_mapped.append((start_outer, end_outer))

            to_map = still_not_mapped
        return mapped + to_map

def part_two(data):
    sections = data.split("\n\n")
    seed_in = list(map(int, sections[0].split(":")[1].split()))
    # note that our seed_ranges are [start, end)
    seed_ranges = [(start, start + num_seeds)  for start, num_seeds in zip(seed_in[::2], seed_in[1::2])]
    mappings = [Mapping(mapping_def) for mapping_def in sections[1:]]

    min_vals = []
    for seed_start, seed_end in seed_ranges:
        ranges = [(seed_start, seed_end)]
        for mapping in mappings:
            ranges = mapping.map_ranges(ranges)
        min_vals.append(min([r[0] for r in ranges]))
    return min(min_vals)

if __name__ == "__main__":
    data = get_data(day=5, year=2023)
    # print(f"{part_one(data)=}")
    print(f"{part_two(data)=}")

    
