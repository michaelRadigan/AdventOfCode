use std::{collections::VecDeque};

use itertools::Itertools;

pub fn part1(input: &str) -> usize {

    let (crates_setup, movements) = input.split("\n\n").collect_tuple().unwrap();

    let mut stacks: [Vec<char>; 9] = Default::default();

    
    crates_setup
    .lines()
    .rev()
    .skip(1)
    .for_each(|line| {
        line
        .chars()
        .skip(1)
        .step_by(4)
        .enumerate()
        .filter(|(_, c)| !c.is_whitespace())
        .for_each(|(i, c)| {
            stacks[i].push(c);
        });
    });
    
    movements
    .lines()
    .for_each(|line| {
        let (number, from, to) = 
            line
            .split(' ')
            .skip(1)
            .step_by(2)
            .map(|c| c.parse::<usize>().unwrap())
            .collect_tuple().unwrap();
        for _ in 0..number {
            let c = stacks[from-1].pop().unwrap();
            stacks[to-1].push(c);
        }
    });
    let res : String = stacks.map(|mut stack| stack.pop().unwrap()).into_iter().collect();
    println!("{:?}", res);

    0
}

//                 [B] [L]     [J]    
//             [B] [Q] [R]     [D] [T]
//             [G] [H] [H] [M] [N] [F]
//         [J] [N] [D] [F] [J] [H] [B]
//     [Q] [F] [W] [S] [V] [N] [F] [N]
// [W] [N] [H] [M] [L] [B] [R] [T] [Q]
// [L] [T] [C] [R] [R] [J] [W] [Z] [L]
// [S] [J] [S] [T] [T] [M] [D] [B] [H]
//  1   2   3   4   5   6   7   8   9 

pub fn part2(input: &str) -> usize {

    let (crates_setup, movements) = input.split("\n\n").collect_tuple().unwrap();

    let mut stacks: [Vec<char>; 9] = Default::default();

    
    crates_setup
    .lines()
    .rev()
    .skip(1)
    .for_each(|line| {
        line
        .chars()
        .skip(1)
        .step_by(4)
        .enumerate()
        .filter(|(_, c)| !c.is_whitespace())
        .for_each(|(i, c)| {
            stacks[i].push(c);
        });
    });
    
    movements
    .lines()
    .for_each(|line| {
        let (number, from, to) = 
            line
            .split(' ')
            .skip(1)
            .step_by(2)
            .map(|c| c.parse::<usize>().unwrap())
            .collect_tuple().unwrap();
        let mut v : Vec<char> = Default::default();
        for _ in 0..number {
            let c = stacks[from-1].pop().unwrap();
            v.push(c);
        }
        for c in v.iter().rev() {
            stacks[to-1].push(*c);
        }
    });
    let res : String = stacks.map(|mut stack| stack.pop().unwrap()).into_iter().collect();
    println!("{:?}", res);

    0
}