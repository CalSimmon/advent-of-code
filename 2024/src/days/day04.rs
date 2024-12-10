use std::collections::{HashMap, HashSet};

use crate::utilities::input::read_input;

fn parse_input(day: u8, prac: bool) -> HashMap<String, HashSet<(usize, usize)>> {
    let data = read_input(day, prac);
    let mut map: HashMap<String, HashSet<(usize, usize)>> = HashMap::new();

    for (x, line) in data.iter().enumerate() {
        for (y, c) in line.char_indices() {
            map.entry(c.to_string())
                .or_insert_with(HashSet::new)
                .insert((x, y));
        }
    }
    map
}

fn directions() -> [(i32, i32); 8] {
    let dirs = [
        (-1, 0),
        (-1, 1),
        (0, 1),
        (1, 1),
        (1, 0),
        (1, -1),
        (0, -1),
        (-1, -1),
    ];

    dirs
}

fn x_directions() -> [((i32, i32), (i32, i32)); 2] {
    let dirs = [
        ((-1, -1),(1, 1)),
        ((1, -1),(-1, 1)),
    ];

    dirs
}

fn add_usize(u: usize, i: i32) -> Option<usize> {
    if i.is_negative() {
        u.checked_sub(i.wrapping_abs() as u32 as usize)
    } else {
        u.checked_add(i as usize)
    }
}

fn word_search(data: &HashMap<String, HashSet<(usize, usize)>>, dir: (i32, i32), loc: &(usize, usize), mut i: usize) -> bool {
    let letters = ["X", "M", "A", "S"];
    let new_loc = match (add_usize(loc.0, dir.0), add_usize(loc.1, dir.1)) {
        (Some(x), Some(y)) => {
            (x, y)
        },
        _ => return false,
    };

    if data.get(letters[i]).unwrap().contains(&new_loc) {
        if i < 3 {
            i += 1;
            if word_search(data, dir, &new_loc, i) {
                return true;
            }
        }
        else {
            return true;
        }
    }
    false
}

fn x_search(data: &HashMap<String, HashSet<(usize, usize)>>, loc: &(usize, usize)) -> bool {
    for pair in x_directions() {
        let new_loc = match (add_usize(loc.0, pair.0.0), add_usize(loc.1, pair.0.1)) {
            (Some(x), Some(y)) => {
                (x, y)
            },
            _ => return false,
        };

        match (data.get("M").unwrap().contains(&new_loc), data.get("S").unwrap().contains(&new_loc)) {
            (true, false) => {
                let new_loc = match (add_usize(loc.0, pair.1.0), add_usize(loc.1, pair.1.1)) {
                    (Some(x), Some(y)) => {
                        (x, y)
                    },
                    _ => return false,
                };

                if !data.get("S").unwrap().contains(&new_loc) {
                    return false
                }
            },
            (false, true) => {
                let new_loc = match (add_usize(loc.0, pair.1.0), add_usize(loc.1, pair.1.1)) {
                    (Some(x), Some(y)) => {
                        (x, y)
                    },
                    _ => return false,
                };

                if !data.get("M").unwrap().contains(&new_loc) {
                    return false
                }
            },
            _ => return false
        }
    }

    true
}

fn part_one_solution(data: &HashMap<String, HashSet<(usize, usize)>>) -> i64 {
    let mut total: i64 = 0;
    for x in data.get("X").unwrap() {
        for dir in directions() {
            total += word_search(data, dir, x, 1) as i64;
        }
    }
    total
}

fn part_two_solution(data: &HashMap<String, HashSet<(usize, usize)>>) -> i64 {
    let mut total: i64 = 0;
    for x in data.get("A").unwrap() {
        total += x_search(data, x) as i64;
    }
    total
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let data: HashMap<String, HashSet<(usize, usize)>> = parse_input(day, prac);

    let sol1: i64 = part_one_solution(&data);
    let sol2: i64 = part_two_solution(&data);

    (sol1, sol2)
}