use std::fs::read_to_string;
use std::cmp;

fn read_lines(filename: &str) -> Vec<String> {
    let mut result = Vec::new();

    for line in read_to_string(filename).unwrap().lines() {
        result.push(line.to_string());
    }

    result
}


fn solve_part_one(lines: Vec<String>) -> u32 {
    let mut id_sum = 0;

    for line in lines.iter() {
        id_sum += check_cube_config(line);
    }

    id_sum
}


fn check_cube_config(line: &String) -> u32 {
    let id_games: Vec<&str> = line.split(": ").collect();
    let id: &str = id_games[0].split(" ").nth(1).unwrap();

    let mut is_valid_game = true;

    for curr_game in id_games[1].split("; ") {
        for cube in curr_game.split(", ") {
            let quantity = cube.split(" ").nth(0).unwrap().parse::<u32>().unwrap();
            let color = cube.split(" ").nth(1).unwrap();

            match color {
                "red" => if quantity > 12 {is_valid_game = false;},
                "green" => if quantity > 13 {is_valid_game = false;},
                "blue" => if quantity > 14 {is_valid_game = false;},
                _ => panic!("Invalid"),
            }
        }
    }

    return if is_valid_game { id.parse::<u32>().unwrap() } else { 0 };
}

fn solve_part_two(lines: Vec<String>) -> u32 {
    let mut id_sum = 0;

    for line in lines.iter() {
        id_sum += get_minimum_cube_config(line);
    }

    id_sum
}


fn get_minimum_cube_config(line: &String) -> u32 {
    let games = line.split(": ").nth(1).unwrap();

    let mut red = 0;
    let mut green = 0;
    let mut blue = 0;

    for curr_game in games.split("; ") {
        for cube in curr_game.split(", ") {
            let quantity = cube.split(" ").nth(0).unwrap().parse::<u32>().unwrap();
            let color = cube.split(" ").nth(1).unwrap();

            match color {
                "red" => red = cmp::max(red, quantity),
                "green" => green = cmp::max(green, quantity),
                "blue" => blue = cmp::max(blue, quantity),
                _ => panic!("Invalid"),
            }
        }
    }

    red * green * blue
}



fn main() {
    //let lines = read_lines("small_input.txt");
    let lines = read_lines("input.txt");

    let total_sum = solve_part_one(lines.clone());
    println!("Part 1: {total_sum}");

    let part_two_res = solve_part_two(lines);
    println!("Part 2: {part_two_res}");
}
