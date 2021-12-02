def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    f = lambda x: [x[0], int(x[1])]
    return map(f, [x.strip("\n").split(" ") for x in content])


def solve_part_one(directions):
    curr_x = 0
    curr_y = 0
    for step, size in directions:
        if step == "forward":
            curr_x += size
        elif step == "down":
            curr_y += size
        elif step == "up":
            curr_y -= size

    return curr_x * curr_y


def solve_part_two(directions):
    curr_x = 0
    curr_y = 0
    aim = 0
    for step, size in directions:
        if step == "forward":
            curr_x += size
            curr_y += aim * size
        if step == "down":
            aim += size
        if step == "up":
            aim -= size

    return curr_x * curr_y


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))

