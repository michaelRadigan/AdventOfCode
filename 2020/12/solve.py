from aocd.models import Puzzle
from enum import Enum


class Direction(Enum):
    L = 1,
    R = 2,
    F = 3
    N = 4,
    E = 5,
    S = 6,
    W = 7


def parse_line(line):
    # Not going to sanitise here, please forgive me
    direction = Direction[line[0]]
    magnitude = int(line[1:])
    return (direction, magnitude)


def solve_a(commands):
    orientation = 1, 0
    x = 0
    y = 0
    # This is when you really start to wish that python had a switch statement
    for direction, magnitude in commands:
        # First, deal with the easy ones
        if direction == Direction.N:
            y += magnitude
        elif direction == direction.E:
            x += magnitude
        elif direction == direction.S:
            y -= magnitude
        elif direction == direction.W:
            x -= magnitude
        elif direction == direction.F:
            x += orientation[0] * magnitude
            y += orientation[1] * magnitude
        elif direction == direction.L:
            if magnitude == 90:
                orientation = -orientation[1], orientation[0]
            elif magnitude == 180:
                orientation = -orientation[0], -orientation[1]
            elif magnitude == 270:
                orientation = orientation[1], -orientation[0]
            else:
                raise Exception("This should never happen: L")
        elif direction == direction.R:
            if magnitude == 90:
                orientation = orientation[1], -orientation[0]
            elif magnitude == 180:
                orientation = -orientation[0], -orientation[1]
            elif magnitude == 270:
                orientation = -orientation[1], orientation[0]
            else:
                raise Exception("This should never happen: R")
    return abs(x) + abs(y)


def solve_b(commands):
    # Clearly lots of sad redundancy between here and part 1
    orientation = 10, 1
    x = 0
    y = 0
    # This is when you really start to wish that python had a switch statement
    for direction, magnitude in commands:
        # First, deal with the easy ones
        if direction == Direction.N:
            orientation = orientation[0], orientation[1] + magnitude
        elif direction == direction.E:
            orientation = orientation[0] + magnitude, orientation[1]
        elif direction == direction.S:
            orientation = orientation[0], orientation[1] - magnitude
        elif direction == direction.W:
            orientation = orientation[0] - magnitude, orientation[1]
        elif direction == direction.F:
            x += orientation[0] * magnitude
            y += orientation[1] * magnitude
        elif direction == direction.L:
            if magnitude == 90:
                orientation = -orientation[1], orientation[0]
            elif magnitude == 180:
                orientation = -orientation[0], -orientation[1]
            elif magnitude == 270:
                orientation = orientation[1], -orientation[0]
            else:
                raise Exception("This should never happen: L")
        elif direction == direction.R:
            if magnitude == 90:
                orientation = orientation[1], -orientation[0]
            elif magnitude == 180:
                orientation = -orientation[0], -orientation[1]
            elif magnitude == 270:
                orientation = -orientation[1], orientation[0]
            else:
                raise Exception("This should never happen: R")
    return abs(x) + abs(y)


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=12)
    commands = list(map(parse_line, puzzle.input_data.splitlines()))
    answer_a = solve_a(commands)
    print(f"{answer_a=}")
    puzzle.answer_a = answer_a
    answer_b = solve_b(commands)
    print(f"{answer_b=}")
    puzzle.answer_b = answer_b
