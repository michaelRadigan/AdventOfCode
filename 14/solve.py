from aocd.models import Puzzle
import re

# I hate regex so much
regex = re.compile(r'mem\[(\d+)\] = (\d+)')


# Same nonsense as day 5
mappings = str.maketrans({'1': '0', 'X': '1'})

# I hate myself that I've written this hahaha


def replace(i, s, c):
    return s[:i] + c + s[i+1:]


def solve_a(lines):
    set_memory = dict()
    for line in lines:
        if line.split()[0] == "mask":
            mask = line[7:]
            zero_mask = int(mask.translate(mappings), 2)
            override_mask = int(mask.replace('X', '0'), 2)
        else:
            matches = regex.findall(line)
            mem, val = int(matches[0][0]), int(matches[0][1])
            zeroed_val = val & zero_mask
            overriden_val = zeroed_val | override_mask
            set_memory[mem] = overriden_val
    return sum(set_memory.values())

# There's probably a nicer recursive solution but this is just a very ugly, adjusted bfs
# which I think is kind of fine


def get_all_mems(mem, mask):
    all_mems = []
    final_mems = []
    masked_mem = mem
    # First, we're going to replace all of the relevant values in the base
    for i, bit in enumerate(mask):
        if bit == 'X' or bit == '1':
            masked_mem = replace(i, masked_mem, bit)

    # Now, we need to replace each X with both a 0 and a 1
    all_mems.append(masked_mem)

    while all_mems:
        current_mem = all_mems.pop()
        had_x = False
        for i, bit in enumerate(current_mem):
            if bit == 'X':
                had_x = True
                all_mems.append(replace(i, current_mem, str(0)))
                all_mems.append(replace(i, current_mem, str(1)))
                break
        if not had_x:
            final_mems.append(int(current_mem, 2))
    return final_mems


def solve_b(lines):
    set_memory = dict()
    for line in lines:
        if line.split()[0] == "mask":
            mask = line[7:]
            zero_mask = int(mask.translate(mappings), 2)
            override_mask = int(mask.replace('X', '0'), 2)
        else:
            matches = regex.findall(line)
            mem, val = int(matches[0][0]), int(matches[0][1])
            mem = '{:036b}'.format(mem)
            all_mems = get_all_mems(mem, mask)
            all_addrs = list(get_all_addrs(mem, mask))
            for mem in all_mems:
                set_memory[mem] = val

    return sum(set_memory.values())


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=14)
    lines = puzzle.input_data.splitlines()

    answer_a = solve_a(lines)
    print(answer_a)
    puzzle.answer_a = answer_a
    answer_b = solve_b(lines)
    print(answer_b)
    puzzle.answer_b = answer_b
