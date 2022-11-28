extern crate aoc_runner;

#[macro_use]
extern crate aoc_runner_derive;

pub mod day1;

aoc_lib!{ year = 2021 }

pub fn add(left: usize, right: usize) -> usize {
    left + right
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn it_works() {
        let result = add(2, 2);
        assert_eq!(result, 4);
    }
}
