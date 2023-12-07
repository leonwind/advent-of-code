use std::fs::read_to_string;


fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()
        .lines() 
        .map(String::from) 
        .collect() 
}


fn split_line(line: &String, prefix: &str) -> Vec<usize> {
    let (_, values) = line.split_once(prefix).unwrap();
    values.split_whitespace().map(|n| n.parse().unwrap()).collect::<Vec<usize>>()
}


fn split_line_single_value(line: &String, prefix: &str) -> usize {
    let (_, values) = line.split_once(prefix).unwrap();
    values.replace(" ", "").parse().unwrap()
}


fn solve_part_one(lines: &Vec<String>) -> usize {
    let times = split_line(&lines[0], "Time:");
    let distances = split_line(&lines[1], "Distance:");
    
    let mut result = 1;

    for (time, distance) in times.iter().zip(distances.iter()) {
        let mut count = 0;
        for hold_time in 1..*time {
            let run_distance = (time - hold_time) * hold_time;
            count += (run_distance > *distance) as usize;
        }
        result *= count;
    }

    result
}


fn solve_part_two(lines: &Vec<String>) -> usize {
    let time = split_line_single_value(&lines[0], "Time:");
    let distance = split_line_single_value(&lines[1], "Distance:");

    let mut result = 0;
    for hold_time in 1..time {
        let run_distance = (time - hold_time) * hold_time;
        result += (run_distance > distance) as usize;
    }

    result 
}


fn main() {
    let lines = read_lines("input.txt");

    let part_one_res = solve_part_one(&lines);
    println!("Part 1: {part_one_res}");

    let part_two_res = solve_part_two(&lines);
    println!("Part 2: {part_two_res}");
}
