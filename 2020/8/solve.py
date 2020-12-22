from aocd.models import Puzzle

if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=8)
    lines = puzzle.input_data.split('\n')

    seen = set()
    instruction_number = 0
    accumulator = 0

    def execute_line(line):
        op, arg = line.split()
        print(op)
        print(arg)

    while instruction_number not in seen:
        line = lines[instruction_number]
        seen.add(instruction_number)
        op, arg = line.split()
        if op == 'acc':
            accumulator += int(arg)
            instruction_number += 1
        elif op == 'jmp':
            instruction_number += int(arg)
        elif op == 'nop':
            instruction_number += 1
    print(accumulator)
    puzzle.answer_a = accumulator
