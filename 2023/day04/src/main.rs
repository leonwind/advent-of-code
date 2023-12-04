use std::{fs::read_to_string, collections::BTreeSet};

struct Card {
    winning: BTreeSet<usize>,
    have: BTreeSet<usize>
}

impl Card {
    fn count_winning(&self) -> usize {
        self.winning.intersection(&self.have).count()
    }

    fn score(&self) -> usize {
        let winning_count = self.count_winning();
        if winning_count > 0 { 1 << (winning_count - 1) } else { 0 }
    }
}

fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()
        .lines() 
        .map(String::from) 
        .collect() 
}


fn solve_part_one(lines: &Vec<String>) -> usize {
    let mut cards = Vec::new();

    for line in lines.iter() {
        let (_, input) = line.split_once(": ").unwrap();
        let (winning_input, have_input) = input.split_once(" | ").unwrap();
        let winning = winning_input.split(" ").filter(|n| !n.is_empty()).map(|n| n.parse().unwrap()).collect();
        let have = have_input.split(" ").filter(|n| !n.is_empty()).map(|n| n.parse().unwrap()).collect();
        cards.push(Card { winning, have });
    }
    
    cards.iter().map(Card::score).sum()
}


fn solve_part_two(lines: &Vec<String>) -> usize {
    let mut cards = Vec::new();

    for line in lines.iter() {
        let (_, input) = line.split_once(": ").unwrap();
        let (winning_input, have_input) = input.split_once(" | ").unwrap();
        let winning = winning_input.split(" ").filter(|n| !n.is_empty()).map(|n| n.parse().unwrap()).collect();
        let have = have_input.split(" ").filter(|n| !n.is_empty()).map(|n| n.parse().unwrap()).collect();
        cards.push(Card { winning, have });
    }

    let mut nums: Vec<usize> = vec![1; cards.len()];
    for (i, c) in cards.iter().enumerate() {
        let winning = c.count_winning();

        for j in i + 1..i + 1 +winning {
            nums[j] += nums[i];
        }
    }

    nums.iter().sum()
}


fn main() {
    let lines = read_lines("input.txt");

    let part_one_res = solve_part_one(&lines);
    println!("Part 1: {part_one_res}");

    let part_two_res = solve_part_two(&lines);
    println!("Part 2: {part_two_res}");
}
