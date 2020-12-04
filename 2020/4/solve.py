import collections
from aocd.models import Puzzle


keys = {"byr:", "iyr:", "eyr:", "hgt:", "hcl:", "ecl:", "pid:"}

# Not reusing keys immediately due to one needing ':' and the other not, should probably clean up
validations = {
    'byr': lambda byr: 1920 <= int(byr) <= 2020,
    'iyr': lambda iyr: 2010 <= int(iyr) <= 2020,
    'eyr': lambda eyr: 2020 <= int(eyr) <= 2030,
    'hgt': lambda hgt: (hgt.endswith('cm') and 150 <= int(hgt[:-2]) <= 193) or (hgt.endswith('in') and 59 <= int(hgt[:-2]) <= 76),
    'hcl': lambda hcl: hcl[0] == '#' and len(hcl) == 7 and all(char.isdigit() or char in 'abcdef' for char in hcl[1:]),
    'ecl': lambda ecl: ecl in {'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'},
    'pid': lambda pid: len(pid) == 9 and pid.isnumeric(),
    'cid': lambda cid: True
}


def solve(passports, is_valid):
    return sum(map(is_valid, passports))


def is_valid_a(passport):
    return all(k in passport for k in keys)


def is_valid_b(passport):
    if not is_valid_a(passport):
        return False
    rules = map(lambda rule: rule.split(':'), passport.split())
    return all(validations[k](v) for k, v in rules)


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=4)
    passports = list((puzzle.input_data.split('\n\n')))
    solution_a = solve(passports, is_valid_a)
    print(f"Part A: {solution_a}")
    puzzle.answer_a = solution_a

    solution_b = solve(passports, is_valid_b)
    print(f"Part B: {solution_b}")
    puzzle.answer_b = solution_b
