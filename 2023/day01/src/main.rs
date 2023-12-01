use std::fs::read_to_string;
use regex::Regex;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string())
    }

    result
}

fn part_one(lines: Vec<String>) -> u32 {
    const RADIX: u32 = 10;

    let mut total_sum = 0;
    for line in lines.iter() {
        let mut first_idx = None;
        let mut last_idx = None;

        for (i, c) in line.chars().enumerate() {
            if c.is_digit(RADIX) {
                if first_idx.is_none() {
                    first_idx = Some(i);
                    last_idx = Some(i);
                } else {
                    last_idx = Some(i);
                }
            }
        }

        total_sum += line.chars().nth(first_idx.unwrap()).unwrap().to_digit(RADIX).unwrap() * 10 + 
            line.chars().nth(last_idx.unwrap()).unwrap().to_digit(RADIX).unwrap();
    }

    return total_sum;
}

fn part_two(lines: Vec<String>) -> u32 {
    let mut total_sum = 0;
    for line in lines.iter() {
        total_sum += solve_line_with_literals(line);
    }

    return total_sum;
}

fn solve_line_with_literals(line: &String) -> u32 {
    let pattern_fwd: Regex =
        Regex::new(r"(\d|one|two|three|four|five|six|seven|eight|nine)").unwrap();
    let pattern_back: Regex =
        Regex::new(r"(\d|eno|owt|eerht|ruof|evif|xis|neves|thgie|enin)").unwrap();

    let first = find_num(pattern_fwd, line.clone());
    let last = find_num(pattern_back, line.chars().rev().collect());
    
    return first * 10 + last;
}

fn map_match(s: &str) -> u32 {
    match s {
        "one" | "eno" => return 1,
        "two" | "owt" => return 2,
        "three" | "eerht" => return 3,
        "four" | "ruof" => return 4,
        "five" | "evif" => return 5,
        "six" | "xis" => return 6,
        "seven" | "neves" => return 7,
        "eight" | "thgie" => return 8,
        "nine" | "enin" => return 9,
        _ => return s.parse::<u32>().unwrap(),
    }
}

fn find_num(pattern: Regex, s: String) -> u32 {
    if let Some(capture) = pattern.captures_iter(&s).nth(0) {
        let token = capture.get(0).unwrap().as_str();
        return map_match(token);
    }
    return 0; 
}


fn main() {
    let lines = read_lines("input.txt");

    let total_sum = part_one(lines.clone());
    println!("Part 1: {total_sum}");

    let total_sum_words = part_two(lines);
    println!("Part 2: {total_sum_words}");
}
