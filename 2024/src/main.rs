mod days;
mod utilities;

use std::env;
use std::time::Instant;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("Please provide a day");
        return;
    }

    let day: u8 = match args[1].parse::<u8>() {
        Ok(num) => num,
        Err(_) => {
            println!("Invalid problem number");
            return;
        }
    };

    let prac = args.contains(&String::from("-p"));

    let mut _runtime = 0.0;
    
    let func: fn(u8, bool) -> (i64, i64) = get_solver(day);

    let time = Instant::now();
    let (p1, p2) = func(day, prac);
    let elapsed_ms = time.elapsed().as_nanos() as f64 / 1_000_000.0;
    
    println!("\n=== Day {:02} ===", day);
    println!("  · Part 1: {}", p1);
    println!("  · Part 2: {}", p2);
    println!("  · Elapsed: {:.4} ms", elapsed_ms);

    _runtime += elapsed_ms;
    
}

fn get_solver(day: u8) -> fn(u8, bool) -> (i64, i64) {
    match day {
        1 => days::day01::solve,
        // Add more cases as needed
        _ => unimplemented!(),
    }
}
