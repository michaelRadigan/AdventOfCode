use std::str::FromStr;

#[derive(Debug, PartialEq)]
pub enum Direction {
    FORWARD,
    UP,
    DOWN
}
pub type Instruction = (Direction, i32);
struct Position {
    x: i32,
    depth: i32,
    aim: i32
}

impl FromStr for Direction {
    type Err = ();

    fn from_str(input: &str) -> Result<Direction, Self::Err> {
        match input {
            "forward" => Ok(Direction::FORWARD),
            "up"  => Ok(Direction::UP),
            "down"  => Ok(Direction::DOWN),
            _      => Err(()),
        }
    }
}
 
#[aoc_generator(day2)]
pub fn input_generator(input: &str) -> Vec<Instruction> {
    input
    .lines()
    .map(|line| {
        let mut ins = line.trim().split(' ');
        let instruction = (
            Direction::from_str(ins.next().unwrap()).unwrap(),
            ins.next().unwrap().parse::<i32>().unwrap(),
        );
        instruction
    })
    .collect()
}

fn solve(instructions: &[Instruction], folder:  fn(Position, &Instruction) -> Position)  -> i32 {
    let final_position = 
        instructions
        .into_iter()
        .fold(Position { x: 0, depth: 0, aim: 0}, folder);
    final_position.x*final_position.depth
}

#[aoc(day2, part1, TWO)]
pub fn part1(instructions: &[Instruction]) -> i32 {
    solve(instructions, |acc: Position, instruction| {
        match instruction {
            | (Direction::FORWARD, distance) => Position {x: acc.x + distance, depth: acc.depth, aim: 0},
            | (Direction::UP, distance) => Position {x: acc.x, depth: acc.depth - distance, aim: 0},
            | (Direction::DOWN, distance) => Position {x: acc.x, depth: acc.depth + distance, aim: 0},
        }
    })
}

#[aoc(day2, part2, TWO)]
pub fn part2(instructions: &[Instruction]) -> i32 {
    solve(instructions, |acc: Position, instruction| {
        match instruction {
            | (Direction::FORWARD, distance) => Position {x: acc.x + distance, depth: acc.depth + distance*acc.aim, aim: acc.aim},
            | (Direction::UP, distance) => Position {x: acc.x, depth: acc.depth, aim: acc.aim - distance},
            | (Direction::DOWN, distance) => Position {x: acc.x, depth: acc.depth, aim: acc.aim + distance},
        }
    })
}
