#[aoc(day1, part1, TWO)]
pub fn part1(input: &str) -> i32 {
    input
    .lines()
    // TODO[michaelr]: Fill me in from here :) :) 
    .into_iter()
    .count()
    .try_into()
    .unwrap()
}