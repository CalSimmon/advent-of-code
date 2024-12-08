use crate::utilities::input::read_input;

use std::cmp::PartialOrd;

fn parse_input(day: u8, prac: bool) -> Vec<String> {
    let data = read_input(day, prac);

    data
}

fn check_next_item(op: fn(i64, i64) -> bool, a: i64, b: i64) -> bool {
    let result = op(a, b);
    
    result
}

fn part_one_solution(data: Vec<String>) -> i64 {
    let answer: Vec<_>  = data
        .iter()
        .filter_map(|s| {
            let seq: Vec<i64> = s
                .split_whitespace()
                .filter_map(|s| s.parse::<i64>().ok())
                .collect::<Vec<_>>();

            match seq.get(0) < seq.get(1) {
                true => {
                    if seq.is_sorted_by(|a, b| b > a && b <= &(a + 3)) {
                        Some(seq)
                    }
                    else {
                        None
                    }
                },
                false => {
                    if seq.is_sorted_by(|a, b| b < a && b >= &(a - 3)) {
                        Some(seq)
                    }
                    else {
                        None
                    }
                }
            }

        })
        .collect();
    
    answer.len().try_into().unwrap()
}

fn part_two_solution(_data: Vec<String>) -> i64 {
    // Add part 2 solution here
    
    0
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: Vec<String>  = parse_input(day, prac);

    println!("1 and 2 result: {}", check_next_item(PartialOrd::gt, 1, 2));

    let sol1: i64 = part_one_solution(data.clone());
    let sol2: i64 = part_two_solution(data.clone());

    (sol1, sol2)
}