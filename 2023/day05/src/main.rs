use std::fs::read_to_string;
use core::ops::Range;
use std::thread;
use std::sync::{Arc, Mutex};

#[derive(Clone)]
struct MapEntry {
    range: Range<usize>,
    offset: i64
}


struct Map {
    entries: Vec<MapEntry>
}


impl Map {
    fn apply(&self, x: usize) -> usize{
        for entry in &self.entries {
            if entry.range.contains(&x) {
                return (x as i64 + entry.offset) as usize;
            }
        }

        x
    }
}


fn read_lines(filename: &str) -> Vec<String> {
    read_to_string(filename) 
        .unwrap()
        .lines() 
        .map(String::from) 
        .collect() 
}


fn parse_start_seeds(line: &String) -> Vec<usize> {
    let (_, seeds) = line.split_once(": ").unwrap();
    seeds.split(" ").map(|seed| seed.parse().unwrap()).collect()
}


fn parse_maps(lines: &[String]) -> Vec<Map>{
    let mut maps = Vec::new();
    
    let mut curr_entries: Vec<MapEntry> = Vec::new();
    for line in lines.iter() {
        if line.contains("map:") {
            continue;
        }

        if line.is_empty() {
            maps.push(Map{ entries: curr_entries.clone() });
            curr_entries.clear();
            continue;
        }

        let mut values = line.split(" ");
        let dest_start: usize = values.next().unwrap().parse().unwrap();
        let source_start: usize = values.next().unwrap().parse().unwrap();
        let len: usize = values.next().unwrap().parse().unwrap(); 

        curr_entries.push(MapEntry{
            range: source_start..source_start + len,
            offset: dest_start as i64 - source_start as i64
        });
    }
    maps.push(Map{ entries: curr_entries.clone() });

    maps
}


fn solve_part_one(lines: &Vec<String>) -> usize {
    let seeds = parse_start_seeds(&lines[0]);
    let maps = parse_maps(&lines[2..]);

    let mut min_location: usize = usize::MAX;

    for mut seed in seeds {
        for map in &maps {
            seed = map.apply(seed);
        }

        min_location = min_location.min(seed);
    }

    min_location
}

fn solve_part_two(lines: &Vec<String>) -> usize {
    let seeds = parse_start_seeds(&lines[0]);
    let maps = parse_maps(&lines[2..]);
    
    let mut min_location = usize::MAX;

    // Not really efficient but still fast enough (< 1min)
    for i in (0..seeds.len()).step_by(2) {
        for mut seed in seeds[i]..seeds[i] + seeds[i + 1] {
            for map in &maps {
                seed = map.apply(seed);
            }

            min_location = min_location.min(seed);
        }
        println!("Finished range {i}");
    }

    min_location 
}


fn solve_part_two_parallel(lines: &Vec<String>) -> usize {
    let seeds = Arc::new(parse_start_seeds(&lines[0]));
    let maps = Arc::new(parse_maps(&lines[2..]));
    
    let min_location = Arc::new(Mutex::new(usize::MAX));

    let threads: Vec<_> = (0..seeds.len()).step_by(2)
        .map(|i| {
            let seeds = seeds.clone();
            let maps = maps.clone();
            let min_location = min_location.clone();

            thread::spawn(move || {
                let mut local_min_location: usize = usize::MAX;
                for mut seed in seeds[i]..seeds[i] + seeds[i + 1] {
                    for map in maps.iter() {
                        seed = map.apply(seed);
                    }

                    local_min_location = local_min_location.min(seed);
                }

                let mut guard = min_location.lock().unwrap();
                *guard = (*guard).min(local_min_location);
                println!("Finished range {i}");
            })
        })
        .collect();

    for thread in threads {
        thread.join().unwrap();
    }

    return *min_location.lock().unwrap();
}


fn main() {
    //let lines = read_lines("small_input.txt");
    let lines = read_lines("input.txt");

    let part_one_res = solve_part_one(&lines);
    println!("Part 1: {part_one_res}");

    //let part_two_res = solve_part_two(&lines);
    let part_two_res = solve_part_two_parallel(&lines);
    println!("Part 2: {part_two_res}");
}
