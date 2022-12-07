use itertools::Itertools;

fn find_marker(input: &str, n : usize) -> usize{
    let (start_index, window) = 
        input
        .as_bytes()
        .windows(n)
        .enumerate()
        .find(|(_, window)| window.iter().unique().count() == n)
        .unwrap();

    println!("{:?}", window);
    start_index + n
}

pub fn part1(input: &str) -> usize {
    find_marker(input, 4)
}

pub fn part2(input: &str) -> usize {
    find_marker(input, 14)
}