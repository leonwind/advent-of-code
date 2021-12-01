def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [int(x.strip("\n")) for x in content]


def solve_part_one(depths):
    total_increments = 0
    prev = depths[0]
    for curr in depths[1:]:
        if curr > prev:
            total_increments += 1
        prev = curr

    return total_increments


def solve_part_two(depths):
    total_increments = 0
    left = 0
    prev_window_sum = depths[0] + depths[1] + depths[2]

    for right in range(3, len(depths)):
        curr_window_sum = prev_window_sum - depths[left] + depths[right]
        if curr_window_sum > prev_window_sum:
            total_increments += 1

        prev_window_sum = curr_window_sum
        left += 1

    return total_increments


if __name__ == "__main__":
    depths = read_input("input.txt")

    print(solve_part_one(depths))
    print(solve_part_two(depths))

