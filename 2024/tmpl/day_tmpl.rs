use crate::utilities::input::read_input;

fn parse_input(day: u8, prac: bool) {
    let data = read_input(day, prac);

    /// Add parsing code here ///
}

fn part_one_solution() -> i64 {
    /// Add part 1 solution here ///
    
    0
}

fn part_two_solution() -> i64 {
    /// Add part 2 solution here ///
    
    0
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: (Vec<i64>, Vec<i64>) = parse_input(day, prac);

    let sol1: i64 = part_one_solution(data.clone());
    let sol2: i64 = part_two_solution(data.clone());

    (sol1, sol2)
}