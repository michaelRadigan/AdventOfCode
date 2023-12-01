from aocd import get_data

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

def part_one(data):
    lines = data.split("\n")
    digits = [get_digits(line) for line in lines]
    return sum([int(d[0] + d[-1]) for d in digits])
    
def part_two(data):
    return part_one(hacky_translate(data))

if __name__ == "__main__":
    data = get_data(day=1, year=2023)
    print(f"{part_one(data)=}")
    print(f"{part_two(data)=}")
