def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    start = rows[0]
    rules = {}
    for row in rows[2:]:
        left, right = row.split(" -> ")
        rules[left] = right
    
    return start, rules


def _run_insertion_process(word, rules, steps):
    patterns = {}
    for i in range(len(word) - 1):
        pattern = word[i] + word[i + 1]
        if pattern in patterns:
            patterns[pattern] += 1
        else:
            patterns[pattern] = 1

    char_count = {}
    for c in word: 
        if c in char_count:
            char_count[c] += 1
        else:
            char_count[c] = 1
    
    for _ in range(steps):
        new_patterns = {}

        for pattern, freq in patterns.items():
            if pattern not in rules:
                new_patterns[pattern] = freq
                continue
            
            middle_char = rules[pattern]
            if middle_char in char_count:
                char_count[middle_char] += freq
            else:
                char_count[middle_char] = freq

            new_left = pattern[0] + middle_char
            new_right = middle_char + pattern[1]
            new_creations = [new_left, new_right]

            for new_creation in new_creations:
                if new_creation in new_patterns:
                    new_patterns[new_creation] += freq
                else:
                    new_patterns[new_creation] = freq

        patterns = new_patterns

    freqs = char_count.values()
    return max(freqs) - min(freqs)


def solve_part_one(word, rules):
    return _run_insertion_process(word, rules, 10)


def solve_part_two(word, rules):
    return _run_insertion_process(word, rules, 40)


if __name__ == "__main__":
    start_word, rules = read_input("input.txt")

    print(solve_part_one(start_word, rules))
    print(solve_part_two(start_word, rules))
