fn parse_assignment(mut assignment: &str) -> (usize, usize) {
    let mut split = assignment.split('-');
    (
        split.next().unwrap().parse::<usize>().unwrap(),
        split.next().unwrap().parse::<usize>().unwrap()
    )
}

fn parse_pair(mut line: &str) -> ((usize, usize), (usize, usize)) {
    let mut split = line.split(',');
    (
        parse_assignment(split.next().unwrap()),
        parse_assignment(split.next().unwrap())
    )
}

pub fn part1(input: &str) -> usize {
    input
    .lines()
    .map(parse_pair)
    .filter(|((a1, a2), (b1, b2))| a1 <= b1 && a2 >= b2 || b1 <= a1 && b2 >= a2)
    .count()
}

pub fn part2(input: &str) -> usize {
    input
    .lines()
    .map(parse_pair)
    .filter(|((a1, a2), (b1, b2))| !(a2 < b1 || b2 < a1))
    .count()
}