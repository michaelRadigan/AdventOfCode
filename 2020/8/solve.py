from aocd.models import Puzzle


def solve_a(lines, swap=-1):
    max = len(lines) - 1
    seen = set()
    instruction_number = 0
    accumulator = 0

    while instruction_number not in seen:
        if instruction_number > max:
            return True, accumulator
        line = lines[instruction_number]
        seen.add(instruction_number)
        op, arg = line.split()

        # This is really ugly but I'm trying to catch up so don't really care
        if swap == instruction_number:
            if op == 'nop':
                op = 'jmp'
            elif op == 'jmp':
                op = 'nop'

        if op == 'acc':
            accumulator += int(arg)
            instruction_number += 1
        elif op == 'jmp':
            instruction_number += int(arg)
        elif op == 'nop':
            instruction_number += 1
    return False, accumulator


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=8)
    lines = puzzle.input_data.split('\n')

    terminated, accumulator = solve_a(lines)
    puzzle.answer_a = accumulator
    print(accumulator)
    for i in range(len(lines)):
        # If the accumulator is not None then we are done
        terminated, accumulator = solve_a(lines, i)
        if terminated:
            print(accumulator)
            puzzle.answer_b = accumulator
            break
