def read_input(filename):
    with open(filename) as f:
        content = f.readlines()
    rows = [x.strip("\n") for x in content]
    
    graph = {}
    for row in rows:
        start, end = row.split("-")
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

        if end in graph:
            graph[end].append(start)
        else:
            graph[end] = [start]

    return graph


def _traverse(curr, graph, visited, path, all_paths):
    if curr in visited:
        return

    if curr == "end":
        all_paths.append(path)
        return
    
    if not curr[0].isupper():
        visited.add(curr)
    path.append(curr)

    for neighbor in graph[curr]:
        _traverse(neighbor, graph, visited.copy(), path[:], all_paths)


def solve_part_one(graph):
    all_paths = []
    _traverse("start", graph, set(), [], all_paths)
    return len(all_paths)


def _traverse_max_two_times(curr, graph, visited, path, all_paths):
    if not curr[0].isupper():
        if curr not in visited:
            visited[curr] = 1
        
        elif max(visited.values()) == 2:
            return
        else:
            visited[curr] += 1 
    
    if curr == "end":
        all_paths.append(path)
        return
    
    path.append(curr)

    for neighbor in graph[curr]:
        if neighbor == "start":
            continue
        _traverse_max_two_times(neighbor, graph, visited.copy(), path[:], all_paths)


def solve_part_two(graph):
    all_paths = []
    _traverse_max_two_times("start", graph, {}, [], all_paths)
    return len(all_paths)


if __name__ == "__main__":
    input_data = read_input("input.txt")

    print(solve_part_one(input_data))
    print(solve_part_two(input_data))
