use std::{str::FromStr};
use itertools::Itertools;

#[derive(Debug, PartialEq, Clone)]
enum Line {
    CD(String),
    LS,
    DIR(String),
    FILE(usize, String),
}

impl FromStr for Line {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        fn parse_file(line: &str) -> Line {
            let (size, name) = line.split(' ').collect_tuple().unwrap();
            Line::FILE(size.parse::<usize>().unwrap(), name.to_owned())
        }
        match &s[..3] {
            "$ c" => Ok(Line::CD(s[5..].to_owned())),
            "$ l" => Ok(Line::LS),
            "dir" => Ok(Line::DIR(s[4..].to_owned())),
            _ => Ok(parse_file(s))
        }
    }
}

fn parse_directory(lines :  &mut impl Iterator<Item = Line>) -> Vec<usize> {
    let mut sum = 0;
    let mut sub_dirs = Vec::new();
    while let Some(line) = lines.next() {
        match line {
            Line::CD(name) if name == ".." => break,
            Line::LS => (),
            Line::DIR(_) => (),
            Line::FILE(size, _) => sum += size,
            Line::CD(_) => {
                sub_dirs.extend(parse_directory(lines));
                sum += sub_dirs.last().unwrap()
            }
        }
    }
    sub_dirs.push(sum);
    sub_dirs
}


pub fn part1(input: &str) -> usize {
    let mut lines = input.lines().map(|line| Line::from_str(line).unwrap());
    parse_directory(&mut lines).into_iter().filter(|x| x <= &100_000).sum()
}

pub fn part2(input: &str) -> usize {
    let mut lines = input.lines().map(|line| Line::from_str(line).unwrap());
    let sizes = parse_directory(&mut lines);

    let root_size = sizes.last().unwrap();
    let free = 70_000_000 - root_size;

    sizes
    .into_iter()
    .filter(|x| (free + x) >= 30_000_000).sorted().next().unwrap()
}