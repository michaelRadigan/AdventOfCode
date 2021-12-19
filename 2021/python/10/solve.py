from aocd.models import Puzzle
from statistics import median

complement = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

correction_scores = {
    '(': 1,
    '[': 2,
    '{': 3,
    '<': 4,
}


def calculate_error_score(line):
    stack = []
    for c in line:
        match c:
            case '(' | '[' | '{' | '<':
                stack.append(c)
            case ')' | ']' | '}' | '>':
                if complement[stack.pop()] != c:
                    return points[c]
    return 0


def solve_a(lines):
    error_score = 0
    for line in lines:
        error_score += calculate_error_score(line)
    return error_score


# Todo: There's a fair bit of repitition here that I should probably clean up!
def calculate_correction_score(line):
    stack = []
    for c in line:
        match c:
            case '(' | '[' | '{' | '<':
                stack.append(c)
            case ')' | ']' | '}' | '>':
                popped = stack.pop()
                if complement[popped] != c:
                    stack.append(popped)
    score = 0
    while stack:
        next = stack.pop()
        score *= 5
        score += correction_scores[next]
    return score


def solve_b(lines):
    filtered_lines = list(filter(
        lambda line: calculate_error_score(line) == 0, lines))
    correction_scores = map(calculate_correction_score, filtered_lines)
    return median(correction_scores)


if __name__ == "__main__":
    lines = puzzle.input_data.split('\n')

    solution_a = solve_a(lines)
    print(f"{solution_a=}")
    #puzzle.answer_a = solution_a

    solution_b = solve_b(lines)
    print(f"{solution_b=}")
    #puzzle.answer_b = solution_b
