from aocd import get_data

data = get_data(day=1, year=2023)

lookup = {
    "one" : "one1one",
    "two" : "two2two",
    "three" : "three3three",
    "four" : "four4four",
    "five" : "five5five",
    "six" : "six6six",
    "seven" : "seven7seven",
    "eight" : "eight8eight",
    "nine" : "nine9nine",
}

def hacky_translate(data):
    for k, v in lookup.items():
        data = data.replace(k, v)
    return data

def get_digits(line):
    return ''.join(d for d in line if d.isdigit())

def part_one(lines):
    digits = [get_digits(line) for line in lines]
    return sum([int(d[0] + d[-1]) for d in digits])
        
def part_two(data):
    return part_one(hacky_translate(data).split("\n"))


if __name__ == "__main__":
    lines = data.split("\n")
    print(f"{part_one(lines)=}")
    print(f"{part_two(data)=}")



