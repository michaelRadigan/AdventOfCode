from collections import defaultdict
from math import prod
from aocd import get_data


def part_one(data: str):
    lines = data.split("\n")
    sum = 0
    for line in lines:
        id_str, games_str = line.split(':')
        game_id = int(id_str.split(' ')[1])
        valid = True
        for round_str in games_str.split(';'):
            for cube_str in round_str.split(','):
                num_cubes_str, cube_colour = cube_str.strip().split(' ')
                num_cubes = int(num_cubes_str)
                if ((cube_colour == 'red' and num_cubes > 12) or
                    (cube_colour == 'green' and num_cubes > 13) or 
                    (cube_colour == 'blue' and num_cubes  > 14)):
                    valid = False
                    break 
        if valid:
            sum += int(game_id)
    return sum

def part_two(data):
    lines = data.split("\n")
    sum = 0
    for line in lines:
        id_str, games_str = line.split(':')
        game_id = int(id_str.split(' ')[1])
        cube_dict = defaultdict(lambda: 0)
        for round_str in games_str.split(';'):
            for cube_str in round_str.split(','):
                num_cubes_str, cube_colour = cube_str.strip().split(' ')
                num_cubes = int(num_cubes_str)
                cube_dict[cube_colour] = max(cube_dict[cube_colour], num_cubes)
        power = prod(cube_dict.values())
        sum += power
    return sum
    
if __name__ == "__main__":
    data = get_data(day=2, year=2023)
    print(f'{part_one(data)=}')
    print(f'{part_two(data)=}')
