use std::fs::File;
use std::{env, fs};
use reqwest::blocking::Client;
use reqwest::StatusCode;
use std::path::Path;
use std::io::Write;
use rust2022::day1;
use rust2022::day2;
use rust2022::day3;
use rust2022::day4;
use rust2022::day5;
use rust2022::day6;
use rust2022::day7;

// For now, going to write everything in main and maybe get a bit messy!

fn request_url(year: usize, day: usize) -> String {
    format!(
        "https://adventofcode.com/{}/day/{}/input",
        year,
        day
    )
}

fn directory(year: usize) -> String {
    format!("input/{}", year)   
}

fn filename(year: usize, day: usize) -> String {
    format!("input/{}/day{}.txt", year, day)
}

fn get_input(year: usize, day: usize) -> String {
    let url = request_url(year, day);
    let session_cookie = env::var("AOC_SESSION").expect("$AOC_SESSION is not set!");
    let client = Client::new();
    let cookie_header = format!("session={}", session_cookie);
    let res = client
        .get(url)
        .header(reqwest::header::COOKIE, cookie_header)
        .send();

    match res {
        Ok(response) => match response.status() {
            StatusCode::OK => {
                let body = response.text().expect("Could not read content from input");
                return body; 
            }
            status_code => 
                panic!("Could not find input for (day: {}), (year: {}). StatusCode {}", day, year, status_code),
        },
        Err(e) => panic!("Failed to get a response: {}", e),
    }    
}

fn main() {
    let year = 2022;
    let day = 7;

    let filename = filename(year, day);
    let filepath = Path::new(&filename);

    if !filepath.exists() {
        let input = get_input(year, day);
        let directory = directory(year);
        fs::create_dir_all(&directory).unwrap_or_else(|_| panic!("Could not create input directory: {}", directory));
        let mut file = File::create(&filename).unwrap_or_else(|_| panic!("Could not create file {}", filename));
        file.write(input.as_bytes()).unwrap_or_else(|_| panic!("Could not write to {}", filename));
    };

    let input = fs::read_to_string(filepath).unwrap();
    println!("{}", input);

    let part_one_solution = day7::part1(&input);
    println!("Part 1: {}", part_one_solution);
    
    let part_two_solution = day7::part2(&input);
    println!("Part 2: {}", part_two_solution)
}