from aocd.models import Puzzle


def game(nums, n):
    seen = {}
    for i, num in enumerate(nums):
        seen[num] = i + 1
    last_answer = nums[-1]
    for i in range(len(nums)+1, n+1):
        if last_answer in seen:
            answer = i - 1 - seen[last_answer]
        else:
            answer = 0
        seen[last_answer] = i - 1
        last_answer = answer
    return answer


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=15)
    nums = list(map(int, puzzle.input_data.split(',')))
    print(nums)
    answer_a = game(nums, 2020)
    print(answer_a)
    puzzle.answer_a = answer_a
    # Is there a quick way to do this that I'm completely missing?
    answer_b = game(nums, 30000000)
    print(answer_b)
    puzzle.answer_b = answer_b
