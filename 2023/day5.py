from aocd import get_data
from dataclasses import dataclass

@dataclass
class SingleMapping:
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
    for seed in seeds:
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
    
    
def part_two(data):
    pass

if __name__ == "__main__":
    data = get_data(day=5, year=2023)
    print(f"{part_one(data)=}")
    
