from aocd.models import Puzzle
from collections import Counter, defaultdict

letters_to_digit = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9
}


def solve_a(input_outputs):
    count = 0
    for _, outputs in input_outputs:
        for digit in outputs:
            # 0 1 2 3 4 5 6 7 8 9
            # 6 2 5 5 4 5 6 3 7 6
            length = len(digit)
            if length == 2 or length == 4 or length == 3 or length == 7:
                count += 1
    return count


def solve(input, output):
    # a b c d e f g
    # 8 6 8 7 4 9 7

    # We can immediately determine b e and f
    # We can immediately determine 1 4 7 8
    # 1 has c f -> gives us c
    # 4 has b c d f so in 4 and occurs in 6 inputs is b, 7 inputs is d
    # 7 has a c f, in 7 not in 1 and occurs 8 times can be a
    # 8 has a b c d e f g. In 8 and occurs 7 times but is not d (in 4) is 7
    mapping = {}

    [char for word in input for char in word]
    occurence_counter = Counter([char for word in input for char in word])

    by_count = defaultdict(set)

    #by_count = {value: key for key, value in occurence_counter.items()}
    for key, value in occurence_counter.items():
        by_count[value].add(key)

    (b_element,) = by_count[6]
    mapping[b_element] = 'b'
    (e_element,) = by_count[4]
    mapping[e_element] = 'e'
    (f_element,) = by_count[9]
    mapping[f_element] = 'f'

    lengths = {len(word): word for word in input}

    # One
    one = lengths[2]
    for char in one:
        # f is already in the mapping!
        if char not in mapping:
            mapping[char] = 'c'
            break

    four = lengths[4]
    for char in four:
        # d and g occur in 7 inputs but only d is in 4!
        by_count[7]
        if char in by_count[7]:
            mapping[char] = 'd'

    seven = lengths[3]
    for char in seven:
        if char not in mapping:
            mapping[char] = 'a'

    eight = lengths[7]
    for char in eight:
        if char not in mapping:
            mapping[char] = 'g'

    digits = ""
    for word in output:
        #translated = [mapping[char] for char in word]
        # []
        translated = ""
        for char in word:
            translated += mapping[char]
        num = letters_to_digit[''.join(sorted(translated))]
        digits += str(num)
    return int(digits)


def solve_b(input_outputs):
    return sum(solve(input, output) for input, output in input_outputs)


if __name__ == "__main__":
    puzzle = Puzzle(year=2021, day=8)

    def parse(line):
        [input, output] = line.split('|')
        return (input.strip().split(' '), output.strip().split(' '))

    inputs_outputs = [parse(line) for line in puzzle.input_data.split('\n')]

    solution_a = solve_a(inputs_outputs)
    print(f"Part A: {solution_a}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(inputs_outputs)
    print(f"Part B: {solution_b}")
    #puzzle.answer_b = solution_b
