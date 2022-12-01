pub fn part1(input: &str) -> u32 {
    let lines = input.lines();

    let mut max : u32 = 0;
    let mut sum = 0;

    for line in lines {
        if line.is_empty() {
            max = std::cmp::max(sum, max);
            sum = 0;
        } else {
            sum += line.parse::<u32>().expect("Could not parse as int");
        }
    };
    max    
}

pub fn part2(input: &str) -> u32 {
    let lines = input.lines();

    let mut calories = Vec::new();
    let mut sum = 0;

    for line in lines {
        if line.is_empty() {
            calories.push(sum);
            sum = 0;
        } else {
            sum += line.parse::<u32>().expect("Could not parse as int");
        }
    };
    calories.sort();
    calories.reverse();
    calories[0]+calories[1]+calories[2]
}