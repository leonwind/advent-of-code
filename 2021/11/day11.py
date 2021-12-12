def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    matrix = [list(map(int, list(height))) for height in rows]
    return matrix 


def _get_neighbors(matrix, i, j):
    neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1),
                (i + 1, j + 1), (i + 1, j - 1), (i - 1, j + 1), (i - 1, j - 1)] 
    return [(i, j) for i, j in neighbors if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])]


def _run_step(matrix):
    flash_stack = []
    flashed = set()
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            matrix[i][j] += 1
            if matrix[i][j] > 9:
                flash_stack.append((i, j))
                flashed.add((i, j))
                matrix[i][j] = 0
    
    while flash_stack:
        i, j = flash_stack.pop()

        for next_i, next_j in _get_neighbors(matrix, i, j):
            if (next_i, next_j) in flashed:
                continue

            matrix[next_i][next_j] += 1
            if matrix[next_i][next_j] > 9:
                flash_stack.append((next_i, next_j))
                flashed.add((next_i, next_j))
                matrix[next_i][next_j] = 0
    
    return len(flashed)


def solve_part_one(matrix, num_steps=100):
    num_flashes = 0
    for _ in range(num_steps):
        num_flashes += _run_step(matrix)
    return num_flashes


def solve_part_two(matrix):
    num_octopus = len(matrix) * len(matrix[0])
    step = 1

    while True:
        num_flashes = _run_step(matrix)
        if num_flashes == num_octopus:
            return step
        step += 1


if __name__ == "__main__":
    input_data = read_input("input.txt")
    # Copy matrix because of pass-by-reference in Python
    second_matrix = [x[:] for x in input_data]

    print(solve_part_one(input_data))
    print(solve_part_two(second_matrix))
