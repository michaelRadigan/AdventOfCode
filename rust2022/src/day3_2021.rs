#[aoc(day3, part1, TONE)]
pub fn part1(input: &str) -> i32 {
    let matrix = input
        .lines()
        .map(|l| l.chars().map(|c| c.to_digit(2).unwrap()))
        .map(|itr| itr.collect::<Vec<u32>>())
        .collect::<Vec<Vec<u32>>>();

    let height = matrix.len();
    let width = matrix[0].len();
    
    println!("{},{}", width, height);

    let mut gamma = 0;
    let mut epsilon = 0;

    for j in 0..height-1 {
        let mut col_sum = 0;
        for i in 0..width-1 {
            //println!("{},{}", j, i);
            col_sum += matrix[j][i]
        }

        let increment = 2_u32.pow((width - j) as u32);
        if col_sum > ((width / 2_usize) as u32) {
            gamma += increment;
        } else {
            epsilon += increment;
        }    
    }
    (gamma*epsilon).try_into().unwrap()
    
}