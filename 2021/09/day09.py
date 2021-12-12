import heapq


def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    matrix = [list(map(int, list(height))) for height in rows]
    return matrix


def _get_neighbors(matrix, i, j):
    neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)] 
    return [(i, j) for i, j in neighbors if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])]


def _get_low_points(matrix):
    low_points = []
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            is_lower = True

            for next_i, next_j in _get_neighbors(matrix, i, j):
                if matrix[next_i][next_j] <= matrix[i][j]:
                    is_lower = False
                    break

            if is_lower:
                low_points.append((i, j))
    
    return low_points


def solve_part_one(matrix):
    risk_level = sum([1 + matrix[i][j] for i, j in _get_low_points(matrix)])
    return risk_level


def solve_part_two(matrix):
    basins = []
    low_points = _get_low_points(matrix)

    for i, j in low_points:
        stack = [(i, j)]
        visited = set()
        curr_basin_size = 0

        while stack:
            i, j = stack.pop()
            if (i, j) in visited:
                continue
            
            curr_basin_size += 1 
            visited.add((i, j))

            for next_i, next_j in _get_neighbors(matrix, i, j):
                if matrix[i][j] < matrix[next_i][next_j] < 9:
                    stack.append((next_i, next_j))

        if len(basins) < 3:
            heapq.heappush(basins, curr_basin_size)
        elif curr_basin_size > basins[0]:
            heapq.heappop(basins)
            heapq.heappush(basins, curr_basin_size)

    return basins[0] * basins[1] * basins[2]


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
