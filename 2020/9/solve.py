from aocd.models import Puzzle

# Part b i sontiguous set of numbers to sum to 14360655


def solve_a(entries, target):
    # We did 2sum in day 1, just copying it as I am lazy
    seen = set()
    for entry in entries:
        partner = target - entry
        if partner in seen:
            return True, partner*entry
        seen.add(entry)
    return False, -1


def solve_b(nums, target):
    # This is a classic leetcode style question
    # We know that sum(i, j) = sum(0,j) - sum(0,i)
    # We also know that all of the input is positive
    sums = [0]
    i = 0
    j = 0
    # Careful here!
    while True:
        current = sums[j] - sums[i]
        if current < target:
            sums.append(sums[-1] + nums[j])
            j += 1
        elif current > target:
            i += 1
        else:
            break
    # Friendly reminder to future me that I spent 15 mins on a off-by-one error here
    subset = nums[i:j]
    print(subset)
    return min(subset) + max(subset)


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=9)
    preamble = 25
    nums = list(map(int, puzzle.input_data.split('\n')))
    for start, target in enumerate(nums[preamble:]):
        available_summands = nums[start:start+preamble]
        target_rechable, _ = solve_a(available_summands, target)
        if not target_rechable:
            print(target)
            puzzle.answer_a = target
            answer_b = solve_b(nums, target)
            print(answer_b)
            puzzle.answer_b = answer_b
            break
