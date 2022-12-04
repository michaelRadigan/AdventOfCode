use std::{str::FromStr, fs::remove_dir};

#[derive(Debug, PartialEq, Copy, Clone)]
enum Selection {
    ROCK = 0,
    PAPER = 1,
    SCISSORS = 2,
}

impl FromStr for Selection {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "A" | "X" => Ok(Selection::ROCK),
            "B" |"Y" => Ok(Selection::PAPER),
            "C" | "Z" => Ok(Selection::SCISSORS),
            _ => Err(())
        }
    }
}


#[derive(Debug, PartialEq, Copy, Clone)]
enum Res {
    LOSE = 0,
    DRAW = 1,
    WIN = 2,
}

impl FromStr for Res {
    type Err = ();
    fn from_str(s: &str) -> Result<Self, Self::Err> {
        match s {
            "X" => Ok(Res::LOSE),
            "Y" => Ok(Res::DRAW),
            "Z" => Ok(Res::WIN),
            _ => Err(())
        }
    }
}

fn remainder(x: isize, y: isize) -> isize {
    let rem = x % y;
    if rem < 0 {rem + y} else {rem}
}

fn score_1(opponent: Selection, me: Selection) -> isize {
    let match_score = remainder((me as isize) - (opponent as isize) + 1, 3) * 3;
    let selection_score = (me as isize) + 1;
    match_score + selection_score
}

pub fn part1(input: &str) -> isize {
    input
    .lines()
    .map(|l| l.split(' '))
    .map(|mut split| {
        (
        Selection::from_str(split.next().unwrap()).unwrap(),
        Selection::from_str(split.next().unwrap()).unwrap(),
    )})
    .map(|(opponent, me)| score_1(opponent, me))
    .sum()    
}

fn score_2(opponent: Selection, result: Res) -> isize {
    let match_score = (result as isize) * 3;
    let selection_score = remainder(result as isize + opponent as isize + 2, 3) + 1;
    match_score + selection_score
}

pub fn part2(input: &str) -> isize {
    input
    .lines()
    .map(|l| l.split(' '))
    .map(|mut split| {
        (
        Selection::from_str(split.next().unwrap()).unwrap(),
        Res::from_str(split.next().unwrap()).unwrap(),
    )})
    .map(|(opponent, me)| score_2(opponent, me))
    .sum()    
}