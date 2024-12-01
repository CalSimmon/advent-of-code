use std::fs::read_to_string;

pub fn read_input(day: u8, test: bool) -> Vec<String> {
    let filename: &str = if test { "test.txt" } else { "input.txt" };
    let path: String = format!("inputs/{:02}/{}", day, filename);
    read_to_string(path)
        .unwrap()
        .lines()
        .map(String::from)
        .collect()
}