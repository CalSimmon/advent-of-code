use crate::utilities::input::read_input;

use std::collections::HashMap;

fn parse_input(day: u8, prac: bool) -> (Vec<i64>, Vec<i64>) {
    let data = read_input(day, prac);

    let (mut first_map, mut second_map): (Vec<i64>, Vec<i64>) = data
        .iter()
        .filter_map(|s| {
            let pairs: Vec<i64> = s
                .split_whitespace()
                .filter_map(|num| num.parse().ok())
                .collect();
            match (pairs.get(0), pairs.get(1)) {
                (Some(first), Some(second)) => Some((*first, *second)),
                _ => None
            }
        })
        .unzip();
    
    first_map.sort();
    second_map.sort();
    (first_map, second_map)
}

fn create_counter(vec: Vec<i64>) -> HashMap<String, i64> {
    let mut counter: HashMap<String, i64> = HashMap::new();
    for key in vec {
        let val = counter.entry(key.to_string()).or_insert(0);
        *val += 1;
    }
    counter
}

fn part_one_solution((first_map, second_map): (Vec<i64>, Vec<i64>)) -> i64 {
    let answer: i64 = first_map
        .iter()
        .zip(second_map.iter())
        .map(|(a, b)| (a - b).abs())
        .sum();
    answer
}

fn part_two_solution((first_map, second_map): (Vec<i64>, Vec<i64>)) -> i64 {
    let counter: HashMap<String, i64> = create_counter(second_map);
    let answer: i64 = first_map
        .iter()
        .map(|i| i * counter.get(&i.to_string()).unwrap_or(&0))
        .sum();
    answer
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: (Vec<i64>, Vec<i64>) = parse_input(day, prac);

    let sol1: i64 = part_one_solution(data.clone());
    let sol2: i64 = part_two_solution(data.clone());

    (sol1, sol2)
}