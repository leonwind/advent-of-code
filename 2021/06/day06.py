def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip("\n") for x in content]


def parse_input(input_data):
    return [int(x) for x in input_data[0].split(',')]


def _run_simulation(initialal_state, num_days):
    states = {i: 0 for i in range(9)}
    for fish in initial_state:
        states[fish] += 1
        
    for _ in range(num_days):
        next_states = {i: 0 for i in range(9)}
        for state, num_fishes in states.items():
            if num_fishes == 0:
                continue

            state -= 1
            if state == -1:
                next_states[6] += num_fishes
                next_states[8] += num_fishes
            else:
                next_states[state] += num_fishes

        states = next_states

    return sum(states.values())


def solve_part_one(initial_state):
    return _run_simulation(initial_state, 80)         


def solve_part_two(initial_state):
    return _run_simulation(initial_state, 256)


if __name__ == "__main__":
    input_data = read_input("input.txt")
    initial_state = parse_input(input_data)

    print(solve_part_one(initial_state))
    print(solve_part_two(input_data))
