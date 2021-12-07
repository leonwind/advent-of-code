def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def parse_input(input_data):
    return [int(x) for x in input_data[0].split(',')]


def solve_part_one(positions):
    positions.sort()
    median = positions[len(positions) // 2]
    return sum([abs(x - median) for x in positions])


def _gauss(x):
    return x * (x + 1) // 2


def solve_part_two(positions):
    avg = sum(positions) / len(positions)
    return sum([_gauss(abs(x - avg)) for x in positions])


if __name__ == "__main__":
    input_data = read_input("input.txt")
    positions = parse_input(input_data)

    print(solve_part_one(positions))
    print(solve_part_two(positions))
