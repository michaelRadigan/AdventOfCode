#[aoc(day1, part1, ONEs3)]
pub fn part1(input: &str) -> i32 {
    let mut last = 100_000;
    input
    .lines()
    .map(|x| x.parse::<i32>().unwrap())
    .fold(0, |acc, x | {
        let new_acc = if x > last {acc + 1 } else {acc}; 
        last = x;
        new_acc
    })
}