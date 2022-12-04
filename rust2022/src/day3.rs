use std::collections::HashSet;
use itertools::Itertools;

fn item_priority(item: char) -> usize {
    if item.is_lowercase() {item as usize - 96} else {item as usize - 38}
}

fn score(line: &str) -> usize {
    let len = line.len();
    let (first_compartment, second_compartment) = line.split_at(len / 2);
    let set : HashSet<char> = first_compartment.chars().collect();
    let item = second_compartment
    .chars()
    .filter(|c| set.contains(c))
    .unique()
    .exactly_one()
    .unwrap();

    item_priority(item)
}

pub fn part1(input: &str) -> usize {
    input
    .lines()
    .map(|line| score(line))
    .sum()
}

fn score2(elves: Vec<&str>) -> usize {
    let mut it = elves.iter();
    let mut set : HashSet<char> = it.next().unwrap().chars().collect();
    let item = *it.fold(set, |mut s, elf| {
        let char_set : HashSet<char> = elf.chars().collect();
        s.retain(|x| char_set.contains(x));
        s
    })
    .iter()
    .unique()
    .exactly_one()
    .unwrap();

    item_priority(item)
}

pub fn part2(input: &str) -> usize {
    input
    .lines()
    .chunks(3)
    .into_iter()
    .map(|chunk| score2(chunk.collect_vec()))
    .sum()
}