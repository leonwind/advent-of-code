use std::fs::read_to_string;
use std::collections::HashMap;


fn read_lines_with_padding(filename: &str) -> Vec<String> {
    const LINE_LENGTH: usize = 142;
    let mut result = Vec::new();

    result.push(".".repeat(LINE_LENGTH));
    for line in read_to_string(filename).unwrap().lines() {
        let padded_string = format!(".{line}.");
        result.push(padded_string.to_string());
    }
    result.push(".".repeat(LINE_LENGTH));

    result
}


fn solve_part_one(lines: &Vec<String>) -> usize {
    const LINE_LENGTH: usize = 142;
    let mut total_sum = 0;

    for (i, line) in lines.iter().enumerate() {
        let mut curr_num_start_idx = Option::None;

        for (j, c) in line.chars().enumerate() {
            if c.is_ascii_digit() {
                if curr_num_start_idx.is_none() {
                    curr_num_start_idx = Some(j);
                }
            } else if let Some(num_start_idx) = curr_num_start_idx {
                if has_neighboring_symbol(lines, i, num_start_idx, j - num_start_idx) {
                    let value: usize = line[num_start_idx..j].parse().unwrap();
                    total_sum += value;
                }
                curr_num_start_idx = None;
            }
        }

        if let Some(num_start_idx) = curr_num_start_idx {
            if has_neighboring_symbol(lines, i, num_start_idx, LINE_LENGTH - num_start_idx) {
                let value: usize = line[num_start_idx..LINE_LENGTH].parse().unwrap();
                total_sum += value;
            }
        }   
    } 

    total_sum
}


fn has_neighboring_symbol(lines: &Vec<String>, line_idx: usize, start: usize, len: usize) -> bool {
    let char_in_front = lines[line_idx].as_bytes()[start - 1];
    let char_behind = lines[line_idx].as_bytes()[start + len];

    if char_in_front != b'.' || char_behind != b'.' {
        return true;
    }

    for i in start - 1..start + len + 1 {
        let char_above = lines[line_idx - 1].as_bytes()[i];
        let char_below = lines[line_idx + 1].as_bytes()[i];

        if char_above != b'.' && !char_above.is_ascii_digit() {
            return true;
        }
        
        if char_below != b'.' && !char_below.is_ascii_digit() {
            return true;
        }
    }
    
    false
}

fn solve_part_two(lines: &Vec<String>) -> usize{
    const LINE_LENGTH: usize = 142;

    let mut stars = HashMap::new();
    for (i, line) in lines.iter().enumerate() {
        for (j, c) in line.chars().enumerate() {
            if c == '*' {
                stars.insert((i, j), (0, 1));
            }
        }
    }

    for (i, line) in lines.iter().enumerate() {
        let mut curr_num_start_idx = Option::None;

        for (j, c) in line.chars().enumerate() {
            if c.is_ascii_digit() {
                if curr_num_start_idx.is_none() {
                    curr_num_start_idx = Some(j);
                }
            } else if let Some(num_start_idx) = curr_num_start_idx {
                let value: usize = line[num_start_idx..j].parse().unwrap();
                check_neighboring_stars(lines, i, num_start_idx, j - num_start_idx, &mut stars, value);
                curr_num_start_idx = None;
            }
        }

        if let Some(num_start_idx) = curr_num_start_idx {
            let value: usize = line[num_start_idx..LINE_LENGTH].parse().unwrap();
            check_neighboring_stars(lines, i, num_start_idx, LINE_LENGTH - num_start_idx, &mut stars, value);
        }   
    }

    let mut total_gear_ratio = 0;
    for (_, value) in stars.into_iter() {
        if value.0 == 2 {
            total_gear_ratio += value.1;
        }
    }

    total_gear_ratio
}

fn check_neighboring_stars(lines: &Vec<String>, line_idx: usize, start: usize, len: usize, 
    stars: &mut HashMap<(usize, usize), (usize, usize)>, value: usize) -> bool {

    let char_in_front = lines[line_idx].as_bytes()[start - 1];
    let char_behind = lines[line_idx].as_bytes()[start + len];

    if char_in_front == b'*' {
        stars.get_mut(&(line_idx, start - 1)).unwrap().0 += 1;
        stars.get_mut(&(line_idx, start - 1)).unwrap().1 *= value;
    }

    if char_behind == b'*' {
        stars.get_mut(&(line_idx, start + len)).unwrap().0 += 1;
        stars.get_mut(&(line_idx, start + len)).unwrap().1 *= value;
    }


    for i in start - 1..start + len + 1 {
        let char_above = lines[line_idx - 1].as_bytes()[i];
        let char_below = lines[line_idx + 1].as_bytes()[i];

        if char_above == b'*' {
            stars.get_mut(&(line_idx - 1, i)).unwrap().0 += 1;
            stars.get_mut(&(line_idx - 1, i)).unwrap().1 *= value;
        }
        
        if char_below == b'*' {
            stars.get_mut(&(line_idx + 1, i)).unwrap().0 += 1;
            stars.get_mut(&(line_idx + 1, i)).unwrap().1 *= value;
        }
    }
    
    false
}


fn main() {
    //let lines = read_lines_with_padding("small_input.txt");
    let lines = read_lines_with_padding("input.txt");

    let part_one_res = solve_part_one(&lines);
    println!("Part 1: {part_one_res}");

    let part_two_res = solve_part_two(&lines);
    println!("Part 2: {part_two_res}");
}
