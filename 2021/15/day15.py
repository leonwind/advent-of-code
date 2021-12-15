import heapq


def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    return [list(map(int, list(row))) for row in rows]


def _get_neighbors(matrix, i, j):
    neighbors = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
    return [(i, j) for i, j in neighbors if 0 <= i < len(matrix) and 0 <= j < len(matrix[0])]


def _run_dijkstra(matrix):
    i = 0
    j = 0
    target = (len(matrix) - 1, len(matrix[0]) - 1)

    heap = [(0, i, j)]
    visited = set()

    while heap:
        risk, i, j = heapq.heappop(heap)
        
        if (i, j) in visited:
            continue

        if (i, j) == target:
            return risk

        visited.add((i, j))
        
        for next_i, next_j in _get_neighbors(matrix, i, j):
            next_cost = risk + matrix[next_i][next_j]
            heapq.heappush(heap, (next_cost, next_i, next_j))


def solve_part_one(matrix):
    return _run_dijkstra(matrix)    


def _expand_matrix(matrix, num_copies=5):
    top = []
    for row in matrix:
        temp = row[:]
        for i in range(1, num_copies):
            temp.extend([(d + i) % 9 if d + i != 9 else 9 for d in row])
        top.append(temp[:])

    expanded = top.copy()
    for i in range(1, num_copies):
        for row in top:
            expanded.append([(d + i) % 9 if d + i != 9 else 9 for d in row])

    return expanded


def solve_part_two(matrix):
    return _run_dijkstra(_expand_matrix(matrix))


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
