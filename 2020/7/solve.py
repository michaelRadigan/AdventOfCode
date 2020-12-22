import collections
from aocd.models import Puzzle
import functools
import re
from functools import cached_property

# We've fallen a few weeks behind so code quality is going to be very poor until we catch up, be warned


def bfs(graph, node):
    # Well doing bfs for part A was unlucky as part 2 needs dfs, leaving it in because why not?
    queue = []
    queue.append(node)
    visited = set()
    visited.add(node)
    while queue:
        current = queue.pop(0)
        for inner in graph[current]:
            if inner not in visited:
                queue.append(inner)
                visited.add(inner)

    # Don't want to include starting node!
    return len(visited) - 1


if __name__ == "__main__":
    puzzle = Puzzle(year=2020, day=7)

    # I hate dong this so much but it's needed in this case
    regex = re.compile(r'(\d+) ([\w ]+) bags?[.,]')
    contained_by = collections.defaultdict(set)
    contains = collections.defaultdict(set)
    lines = puzzle.input_data.split('\n')

    def process_line(line):
        bag, directly_contains_raw = line.split(' bags contain ')
        directly_contains = regex.findall(directly_contains_raw)
        for num, inner_bag in directly_contains:
            contained_by[inner_bag].add(bag)
            contains[bag].add((int(num), inner_bag))

    [process_line(line) for line in lines]
    answer_a = bfs(contained_by, 'shiny gold')

    # Dear self, please clean up this monstrocity once you've caught up...
    @functools.lru_cache()
    def dfs(node):
        acc = 0
        for num, inner_node in contains[node]:
            acc += num * (1 + dfs(inner_node))
        return acc

    answer_b = dfs('shiny gold')

    puzzle.answer_a = answer_a
    puzzle.answer_b = answer_b
