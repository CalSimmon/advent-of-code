use crate::utilities::input::read_input;

use std::cmp::PartialOrd;
use std::ops;

fn parse_input(day: u8, prac: bool) -> Vec<String> {
    let data = read_input(day, prac);
    data
}

fn compare(a: &i64, b: &i64, f: fn(&i64, &i64) -> bool, g: fn(&i64, &i64) -> bool, h: fn(i64, i64) -> i64) -> bool {
    f(b, a) && g(b, &(h(*a, 3)))
}

fn find_sorted(seq: &Vec<i64>) -> bool {
    let (f, g, h) = find_direction(seq.get(0).unwrap(), seq.get(1).unwrap());
    let result = seq.is_sorted_by(|a, b| compare(a, b, f, g, h));
    result
}

fn find_direction(a: &i64, b: &i64) -> (fn(&i64, &i64) -> bool, fn(&i64, &i64) -> bool, fn(i64, i64) -> i64) {
    match a < b {
        true => {
            (PartialOrd::gt, PartialOrd::le, ops::Add::add)
        },
        false => {
            (PartialOrd::lt, PartialOrd::ge, ops::Sub::sub)

        }
    }
}

fn alter_vector(seq: &Vec<i64>) -> bool {
    let mut result: bool = false;
    let (f, g, h) = find_direction(seq.get(0).unwrap(), seq.get(1).unwrap()); 
    for (idx, num) in seq.into_iter().enumerate() {
        if idx != 0 {
            if !compare(seq.get(idx - 1).unwrap(), num, f, g, h) {
                for i in [0, 1, 2] {
                    if !(idx < i) {
                        let mut seq_clone = seq.clone();
                        seq_clone.remove(idx - i);
                        result = find_sorted(&seq_clone);
                        if result {
                            break;
                        }
                    }
                }
                break;                    
            }
        }
    }
    result
}

fn get_answers(data: &Vec<String>) -> (Vec<Vec<i64>>, Vec<Vec<i64>>) {
    let (normal, altered): (Vec<Vec<i64>>, Vec<Vec<i64>>) = data.iter().fold(
        (Vec::new(), Vec::new()),
        |(mut v1, mut v2), x| {
            let seq: Vec<i64> = x
                .split_whitespace()
                .filter_map(|s| s.parse::<i64>().ok())
                .collect::<Vec<_>>();

            if find_sorted(&seq) {
                v1.push(seq);
            }
            else if alter_vector(&seq) {
                v2.push(seq);
            }
            (v1, v2)
        }
    );
    (normal, altered)
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: Vec<String>  = parse_input(day, prac);
    let (v1, v2) = get_answers(&data);

    let sol1: i64 = v1.len().try_into().unwrap();
    let sol2: i64 = (v1.len() + v2.len()).try_into().unwrap();

    (sol1, sol2)
}