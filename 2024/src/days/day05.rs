use std::collections::{HashMap, HashSet, VecDeque};

use crate::utilities::input::read_input;

fn split_at_blank<T: Default + PartialEq>(mut vec: Vec<T>) -> (Vec<T>, Vec<T>) {
    if let Some(pos) = vec.iter().position(|x| x == &T::default()) {
        let mut right = vec.split_off(pos);
        right.remove(0);  // Remove the blank row itself
        (vec, right)
    } else {
        (vec, Vec::new())
    }
}

fn topological_sort(deps: &HashMap<i64, HashSet<i64>>) -> Vec<i64> {
    let mut in_degree: HashMap<i64, usize> = HashMap::new();
    let mut graph: HashMap<i64, Vec<i64>> = HashMap::new();
    let mut result = Vec::new();
    let mut queue = VecDeque::new();

    // Initialize in-degree and graph
    for (&node, dependencies) in deps {
        in_degree.entry(node).or_insert(0);
        for &dep in dependencies {
            in_degree.entry(dep).or_insert(0);
            graph.entry(dep).or_default().push(node);
        }
    }

    // Calculate in-degree for each node
    for dependencies in deps.values() {
        for &dep in dependencies {
            *in_degree.entry(dep).or_default() += 1;
        }
    }

    // Add nodes with in-degree 0 to the queue
    for (&node, &degree) in &in_degree {
        if degree == 0 {
            queue.push_back(node);
        }
    }

    // Perform topological sorting
    while let Some(node) = queue.pop_front() {
        result.push(node);
        if let Some(neighbors) = graph.get(&node) {
            for &neighbor in neighbors {
                let degree = in_degree.get_mut(&neighbor).unwrap();
                *degree -= 1;
                if *degree == 0 {
                    queue.push_back(neighbor);
                }
            }
        }
    }

    // Check for cycles
    if result.len() != in_degree.len() {
        panic!("The graph contains a cycle!");
    }

    result
}

fn parse_input(day: u8, prac: bool) -> (HashMap<i64, HashSet<i64>>, Vec<Vec<i64>>) {
    let data = read_input(day, prac);

    let (rules, updates) = split_at_blank(data);
    let mod_rules: HashMap<i64, HashSet<i64>> = rules
        .iter()
        .filter_map(|s|{
            let pairs: Vec<i64> = s
                .split("|")
                .filter_map(|num| num.parse().ok())
                .collect();
            match (pairs.get(0), pairs.get(1)) {
                (Some(key), Some(value)) => Some((*key, *value)),
                _ => None
            }
        })
        .fold(HashMap::new(), |mut acc, (key, value)| {
            acc.entry(key)
                .or_insert_with(HashSet::new)
                .insert(value);
            acc
        });

    let mod_updates: Vec<Vec<i64>> = updates
        .iter()
        .map(|s| s
            .split(",")
            .filter_map(|num| num.parse().ok())
            .collect()
        )
        .collect();


    (mod_rules, mod_updates)
}

fn part_one_solution(rules: &HashMap<i64, HashSet<i64>>, updates: &Vec<Vec<i64>>) -> i64 {
    let mut answer: i64 = 0;
    for manual in updates {
        let mut prev: HashSet<i64> = HashSet::new();
        let mut followed_rules: bool = true;
        for (i, page) in manual.iter().enumerate() {
            if i == 0 {
                prev.insert(*page);
            }
            else {
                if rules.contains_key(page) {
                    let intersection: HashSet<&i64> = prev.intersection(&rules[page]).collect();
                    if !intersection.is_empty() {
                        followed_rules = false;
                        break;
                    }
                }
                prev.insert(*page);
            }
        }
        if followed_rules {
            answer += manual[manual.len() / 2]
        }
    }
    
    answer
}

fn part_two_solution(_rules: &HashMap<i64, HashSet<i64>>, _updates: &Vec<Vec<i64>>) -> i64 {
    // Add part 2 solution here
    
    0
}

pub fn solve(day: u8, prac: bool) -> (i64, i64) {
    let (rules, updates)  = parse_input(day, prac);

    println!("{:?}", topological_sort(&rules));

    let sol1: i64 = part_one_solution(&rules, &updates);
    let sol2: i64 = part_two_solution(&rules, &updates);

    (sol1, sol2)
}