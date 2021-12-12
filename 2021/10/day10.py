def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def solve_part_one(subsystems):
    total_score = 0

    scores = {')': 3, ']': 57, '}': 1197, '>': 25137}
    opening = ('(', '[', '{', '<')
    matching = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for system in subsystems:
        stack = []
        for curr in system:
            if curr in opening:
                stack.append(curr)
            else:
                last_opening = stack.pop()
                if matching[last_opening] != curr:
                    total_score += scores[curr]
                    break

    return total_score


def solve_part_two(subsystems):
    total_scores = []

    scores = {')': 1, ']': 2, '}': 3, '>': 4}
    opening = ('(', '[', '{', '<')
    matching = {'(': ')', '[': ']', '{': '}', '<': '>'}

    for system in subsystems:
        is_incomplete = True
        stack = []

        for curr in system:
            if curr in opening:
                stack.append(curr)
            else:
                last_opening = stack.pop()
                if matching[last_opening] != curr:
                    is_incomplete = False
                    break
        
        if is_incomplete:
            curr_score = 0
            while stack:
                top = stack.pop()
                curr_score = (curr_score * 5) + scores[matching[top]]

            total_scores.append(curr_score)        

    return sorted(total_scores)[len(total_scores) // 2]


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
