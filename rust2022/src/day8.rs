use std::ops::Range;
use std::collections::HashSet;
use std::cmp::max;

pub fn part1(input: &str) -> u32 {
    let grid = 
        input
        .lines()
        .map(|line| {
            line
            .chars()
            .map(|x| x.to_digit(10).unwrap())
            .collect::<Vec<u32>>()
        }).collect::<Vec<Vec<u32>>>();

    let height = grid.len();
    let width = grid[0].len();
    
    // The edges are automatically visible!
    let mut visible= (2 * width + 2 * height - 4) as u32;
    let mut seen = HashSet::new();
    fn count_tallest_from(is: impl Iterator<Item = i32>, js: impl Iterator<Item = i32> + Clone, di : i32, dj: i32, grid: &Vec<Vec<u32>>, seen: &mut HashSet<(i32, i32)>) -> u32 {
        let mut sum = 0;
        let mut tallest_to_edge = grid.clone();

        for i in is {
            for j in js.clone() {
                let current_tree = grid[i as usize][j as usize];
                let tallest_tree_to_edge = tallest_to_edge[(i + di) as usize][(j + dj) as usize];
                if current_tree > tallest_tree_to_edge {
                    if !seen.contains(&(i,j)) {
                        sum += 1;
                        seen.insert((i, j));
                    }                
                }
                tallest_to_edge[i as usize][j as usize] = max(tallest_tree_to_edge, current_tree);
            }
        }
        sum
    }

    let is = 1..(height as i32)-1;
    let js = 1..(width as i32)-1;

    // Tallest from the left
    visible += count_tallest_from(is.clone(), js.clone(), 0, -1, &grid, &mut seen);

    // Tallest from the the right
    visible += count_tallest_from(is.clone(), js.clone().rev(), 0, 1, &grid, &mut seen);

    // Tallest from the top
    visible += count_tallest_from(is.clone(), js.clone(), -1, 0, &grid, &mut seen);

    // Tallest from the bottom
    visible += count_tallest_from(is.clone().rev(), js.clone(), 1, 0, &grid, &mut seen);
    visible
}

pub fn part2(input: &str) -> u32 {
    let grid = 
        input
        .lines()
        .map(|line| {
            line
            .chars()
            .map(|x| x.to_digit(10).unwrap())
            .collect::<Vec<u32>>()
        }).collect::<Vec<Vec<u32>>>();
    let height = grid.len();
    let width = grid[0].len();
    fn get_scenic_score(i: usize, j: usize, grid: &Vec<Vec<u32>>) -> u32 {
        fn score_in_direction(i: i32, j: i32, di: i32, dj: i32, grid: &Vec<Vec<u32>>) -> u32 {
            let height = grid.len() as i32;
            let width = grid[0].len() as i32;
            let current_tree = grid[i as usize][j as usize];
            let mut score = 0;
            let mut cmp_i = i;
            let mut cmp_j = j;
            
            loop {
                cmp_i += di;
                cmp_j += dj;
                let can_see_tree = cmp_i >= 0 && cmp_j >= 0 && cmp_i < height && cmp_j < width;
                if !can_see_tree {
                    break;
                }
                score += 1;
                let current_tree_is_bigger = current_tree > grid[cmp_i as usize][cmp_j as usize];
                if !current_tree_is_bigger {
                    break;
                }
            }
            score
        }

        let up_score = score_in_direction(i as i32, j as i32, -1, 0, &grid);
        let down_score = score_in_direction(i as i32, j as i32, 1, 0, &grid);
        let left_score = score_in_direction(i as i32, j as i32, 0, -1, &grid);
        let right_score = score_in_direction(i as i32, j as i32, 0, 1, &grid);
        up_score*down_score*left_score*right_score
    }

    let mut max_score = 0;
    for i in 0..height {
        for j in 0..width {
            let score = get_scenic_score(i, j, &grid);
            max_score = max(score, max_score);
        }
    };
    max_score
}