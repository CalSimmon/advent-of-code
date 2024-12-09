use crate::utilities::input::read_input;

use regex::Regex;

fn parse_input(day: u8, prac: bool) -> Vec<String> {
    let data = read_input(day, prac);

    data
}

fn regex_dump(data: &Vec<String>) -> Vec<&str> {
    let re = Regex::new(r"mul\((\d*,\d*)\)|(do\(\))|(don't\(\))").unwrap();

    let mut results = vec![];
    for line in data {
        for matched in re.captures_iter(line) {
            let full_match = matched.get(0).unwrap().as_str();
            match full_match {
                m if m.starts_with("mul") => results.push(matched.get(1).unwrap().as_str()),
                "do()" => results.push(matched.get(2).unwrap().as_str()),
                "don't()" => results.push(matched.get(3).unwrap().as_str()),
                _ => continue
            }
        }
    }

    results
}

fn part_one_solution(data: &Vec<&str>) -> i64 {
    let answer = data
        .iter()
        .filter_map(|s|
            match s {
                &"do()" => None,
                &"don't()" => None,
                _ => {
                    let split_string: Vec<&str> = s.split(',').collect();
                    Some(split_string[0].parse::<i64>().unwrap() * split_string[1].parse::<i64>().unwrap())
                }
            }
        )
        .sum();

    answer
}

fn part_two_solution(data: &Vec<&str>) -> i64 {
    let mut stop = false;
    let answer = data
        .iter()
        .filter_map(|s|
            match s {
                &"do()" => {
                    stop = false;
                    None
                },
                &"don't()" => {
                    stop = true;
                    None
                },
                _ => {
                    if !stop {
                        let split_string: Vec<&str> = s.split(',').collect();
                        Some(split_string[0].parse::<i64>().unwrap() * split_string[1].parse::<i64>().unwrap())
                    }
                    else {
                        None
                    }
                }
            }
        )
        .sum();
    
    answer
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: Vec<String> = parse_input(day, prac);

    let parsed_data = regex_dump(&data);

    let sol1: i64 = part_one_solution(&parsed_data);
    let sol2: i64 = part_two_solution(&parsed_data);

    (sol1, sol2)
}