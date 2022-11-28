#[aoc(day1, part1, ONE)]
pub fn part1(input: &str) -> i32 {
    let mut last = 100_000;
    input
    .lines()
    .map(|x| x.parse::<i32>().unwrap())
    .fold(0, |acc, x | {
        let new_acc = if x > last {acc + 1} else {acc}; 
        last = x;
        new_acc
    })
}

#[aoc(day1, part2, ONE)]
pub fn part2(input: &str) -> i32 {
    let mut last = 100_000;
    input
    .lines()
    .map(|x| x.parse::<i32>().unwrap())
    .collect::<Vec<i32>>()
    .windows(3)
    // This map feels a little bit ugly to be honest!
    .map(|triple| triple[0] + triple[1] + triple[2])
    .fold(0, |acc, x | {
        let new_acc = if x > last {acc + 1 } else {acc}; 
        last = x;
        new_acc
    })
}