use itertools::Itertools;

fn sum_elves(input: &str) -> impl Iterator<Item = u32> + '_ {
    input
    .split("\n\n")
    .map(|elf| {
        elf
        .lines()
        .map(|line| line.parse::<u32>().unwrap_or(0))
        .sum::<u32>()
    })
}

pub fn part1(input: &str) -> u32 {
    sum_elves(input)
    .max()
    .unwrap()
}

pub fn part2(input: &str) -> u32 {
    sum_elves(input)
    .sorted()
    .rev()
    .take(3)
    .sum::<u32>()
}