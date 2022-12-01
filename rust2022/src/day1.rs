use itertools::Itertools;

pub fn part1(input: &str) -> u32 {
    input
    .split("\n\n")
    .map(|elf| {
        elf
        .lines()
        .map(|line| line.parse::<u32>().unwrap_or(0))
        .sum::<u32>()
    })
    //.collect::<Vec<u32>>()
    .into_iter()
    .max()
    .unwrap()
}

pub fn part2(input: &str) -> u32 {
    input
    .split("\n\n")
    .map(|elf| {
        elf
        .lines()
        .map(|line| line.parse::<u32>().unwrap_or(0))
        .sum::<u32>()
    })
    //.collect::<Vec<u32>>()
    .into_iter()
    .sorted()
    .rev()
    .take(3)
    .sum::<u32>()
}